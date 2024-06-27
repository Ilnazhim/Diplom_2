import allure
import requests
from src import Urls


class Orders:
    @staticmethod
    @allure.step('Отправить запрос на создание заказа')
    def create_order(user_response, ingredients):
        access_token = user_response.json()["accessToken"]
        create_order = requests.post(Urls.BASE_URL + Urls.ORDER_URL, ingredients,
                                     headers={'Authorization': access_token})
        return create_order

    @staticmethod
    @allure.step('Отправить запрос на создание заказа без токена авторизации')
    def create_order_without_auth(ingredients):
        create_order = requests.post(Urls.BASE_URL + Urls.ORDER_URL, ingredients)
        return create_order

    @staticmethod
    @allure.step('Отправить запрос на получение списка заказов пользователя')
    def get_orders(user_response):
        access_token = user_response.json()["accessToken"]
        get_orders = requests.get(Urls.BASE_URL + Urls.ORDER_URL,
                                  headers={'Authorization': access_token})
        return get_orders

    @staticmethod
    @allure.step('Отправить запрос на получение списка заказов пользователя без токена авторизации')
    def get_orders_without_auth():
        get_orders = requests.get(Urls.BASE_URL + Urls.ORDER_URL)
        return get_orders
