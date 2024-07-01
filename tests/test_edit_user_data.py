import allure
import pytest
from modules.auth import Auth
from helper import UserData
from src import Messages


class TestEditUserData:
    @allure.title('Изменение данных пользователя: с авторизацией')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('email', id='test editing email field'),
                                 pytest.param('password', id='test editing password field'),
                                 pytest.param('name', id='test editing name field')
                             ]
                             )
    def test_edit_user(self, field, create_user, delete_user):
        user_body = UserData.generate_fake_user_data()
        new_field = {field: 'changes' + str(user_body[field])}
        edit_user_data = Auth.edit_user_data(create_user, new_field)

        assert edit_user_data.status_code == 200
        assert edit_user_data.json()['success'] is True

    @allure.title('Изменение данных пользователя: без авторизации')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('email', id='тест с полем email'),
                                 pytest.param('password', id='тест с полем password'),
                                 pytest.param('name', id='тест с полем name')
                             ]
                             )
    def test_edit_user_without_auth(self, field, delete_user):
        user_body = UserData.generate_fake_user_data()
        new_field = {field: 'changes' + str(user_body[field])}
        edit_user_data = Auth.edit_user_data_without_auth(new_field)

        assert edit_user_data.status_code == 401
        assert edit_user_data.json()['message'] == Messages.WITHOUT_AUTH
