class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    AUTH_URL = '/api/auth/register'
    DELETE_USER_URL = '/api/auth/user'
    LOGIN_URL = '/api/auth/login'
    EDIT_USER_URL = '/api/auth/user'
    ORDER_URL = '/api/orders'


class Messages:
    EXISTING_USER = 'User already exists'
    REQUIRED_FIELDS = 'Email, password and name are required fields'
    INCORRECT_DATA = 'email or password are incorrect'
    WITHOUT_AUTH = 'You should be authorised'
    ORDER_WITHOUT_INGRD = 'Ingredient ids must be provided'
