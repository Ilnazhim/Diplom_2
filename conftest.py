import pytest
from helper import UserData
from modules.auth import Auth


@pytest.fixture()
def create_user():
    user_body = UserData.generate_fake_user_data()
    user = Auth.create_user(user_body)
    return user


@pytest.fixture()
def delete_user(create_user):
    yield
    Auth.delete_user(create_user)
