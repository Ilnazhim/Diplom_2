import allure
import pytest
from modules.auth import Auth
from helper import UserData
from src import Messages


class TestUserLogin:
    @allure.title('Логин пользователя: логин под существующим пользователем')
    def test_user_login(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        login = Auth.user_login(user_body)

        Auth.delete_user(user)

        assert login.status_code == 200
        assert 'accessToken' in login.json()

    @allure.title('Логин пользователя: логин с неверным логином и паролем')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('email', id='тест с email'),
                                 pytest.param('password', id='тест с password')
                             ]
                             )
    def test_user_login_with_wrong_params(self, field):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        user_body_v2 = user_body.copy()
        user_body_v2[field] = user_body[field] + 'SOMETHING_WRONG'
        login = Auth.user_login(user_body_v2)

        Auth.delete_user(user)

        assert login.status_code == 401
        assert login.json()['message'] == Messages.INCORRECT_DATA
