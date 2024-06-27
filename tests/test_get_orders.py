import allure
from modules.auth import Auth
from modules.orders import Orders
from helper import UserData
from src import Messages
from data import Data


class TestGetOrders:
    @allure.title('Получение заказов конкретного пользователя: с авторизацией')
    def test_get_user_orders(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        Orders.create_order(user, Data.ingredients)
        orders_list = Orders.get_orders(user)

        Auth.delete_user(user)

        assert orders_list.status_code == 200 and 'orders' in orders_list.json()

    @allure.title('Получение заказов конкретного пользователя: без авторизации')
    def test_get_user_orders_without_auth(self):
        orders_list = Orders.get_orders_without_auth()

        assert orders_list.status_code == 401 and orders_list.json()['message'] == Messages.WITHOUT_AUTH
