from modules.auth import Auth
from modules.orders import Orders
from helper import UserData
from src import Messages
from data import Data
import allure


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('Создание заказа с токеном авторизации и корректным списком ингредиентов')
    def test_create_order(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        ingredients = Data.ingredients
        order = Orders.create_order(user, ingredients)
        Auth.delete_user(user)

        assert order.status_code == 200
        assert order.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        ingredients = Data.empty_ingredients
        order = Orders.create_order(user, ingredients)
        Auth.delete_user(user)

        assert order.status_code == 400
        assert order.json()['message'] == Messages.ORDER_WITHOUT_INGRD

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_hash(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        ingredients = Data.invalid_data
        order = Orders.create_order(user, ingredients)
        Auth.delete_user(user)

        assert order.status_code == 500
        assert Messages.INTERNAL_SERVER_ERROR in order.text

    @allure.title('Создание заказа без токена авторизации')
    def test_create_order_without_auth(self):
        ingredients = Data.ingredients
        order = Orders.create_order_without_auth(ingredients)

        assert order.status_code == 200
        assert order.json()['success'] is True
