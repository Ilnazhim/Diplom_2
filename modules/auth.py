import allure
import requests
from src import Urls


class Auth:
    @staticmethod
    @allure.step('Отправить запрос на создание пользователя')
    def create_user(user_body):
        user = requests.post(Urls.BASE_URL + Urls.AUTH_URL, user_body)
        return user

    @staticmethod
    @allure.step('Отправить запрос на удаление пользователя')
    def delete_user(user_response):
        access_token = user_response.json()["accessToken"]
        delete = requests.delete(Urls.BASE_URL + Urls.DELETE_USER_URL, headers={'Authorization': access_token})
        return delete

    @staticmethod
    @allure.step('Отправить запрос на логин пользователя')
    def user_login(user_body):
        login = requests.post(Urls.BASE_URL + Urls.LOGIN_URL, user_body)
        return login

    @staticmethod
    @allure.step('Отправить запрос на изменение данных пользователя')
    def edit_user_data(user_response, field):
        access_token = user_response.json()["accessToken"]
        edit_data = requests.patch(Urls.BASE_URL + Urls.EDIT_USER_URL, field, headers={'Authorization': access_token})
        return edit_data

    @staticmethod
    @allure.step('Отправить запрос на изменение данных пользователя без токена авторизации')
    def edit_user_data_without_auth(field):
        edit_data = requests.patch(Urls.BASE_URL + Urls.EDIT_USER_URL, field)
        return edit_data

