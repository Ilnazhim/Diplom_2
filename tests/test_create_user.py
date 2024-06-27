import allure
import pytest
from modules.auth import Auth
from helper import UserData
from src import Messages


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_user(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)

        Auth.delete_user(user)

        assert user.status_code == 200

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self):
        user_body = UserData.generate_fake_user_data()
        user = Auth.create_user(user_body)
        user_v2 = Auth.create_user(user_body)

        Auth.delete_user(user)

        assert user_v2.status_code == 403 and user_v2.json()['message'] == Messages.EXISTING_USER

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('email', id='тест без указанного поля email'),
                                 pytest.param('password', id='тест без указанного поля  password'),
                                 pytest.param('name', id='тест без указанного поля  name')
                             ]
                             )
    def test_create_courier_without_required_fields(self, field):
        user_body = UserData.generate_fake_user_data().pop(field)
        user = Auth.create_user(user_body)

        assert user.status_code == 403 and user.json()['message'] == Messages.REQUIRED_FIELDS






