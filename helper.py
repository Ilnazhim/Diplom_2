import allure
from faker import Faker


class UserData:

    @staticmethod
    @allure.step('Сгенерировать данные для пользователя')
    def generate_fake_user_data():
        fake = Faker()
        user_body = {
            "email": fake.email(),
            "password": fake.passport_number(),
            "name": fake.user_name()
        }
        return user_body

    @staticmethod
    def delete_field_from_json(body, field):
        new_body = body.pop(field)
        return new_body
