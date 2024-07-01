import allure
from modules.orders import Orders
from src import Messages
from data import Data


class TestGetOrders:
    @allure.title('Получение заказов конкретного пользователя: с авторизацией')
    def test_get_user_orders(self, create_user, delete_user):
        Orders.create_order(create_user, Data.ingredients)
        orders_list = Orders.get_orders(create_user)

        assert orders_list.status_code == 200
        assert 'orders' in orders_list.json()

    @allure.title('Получение заказов конкретного пользователя: без авторизации')
    def test_get_user_orders_without_auth(self):
        orders_list = Orders.get_orders_without_auth()

        assert orders_list.status_code == 401
        assert orders_list.json()['message'] == Messages.WITHOUT_AUTH
