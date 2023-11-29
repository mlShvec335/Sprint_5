import random


class Urls:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    login_url = 'https://stellarburgers.nomoreparties.site/login'
    reg_url = 'https://stellarburgers.nomoreparties.site/register'
    forgot_pass_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
    profile_url = 'https://stellarburgers.nomoreparties.site/account/profile'


class LoginData:
    email = 'shvetsov_3@yandex.ru'
    password = '1234567'
    name = 'test'
    random_email = f'shvetsov_{random.randint(1000, 9999)}@mail.ru'
    invalid_password = '12345'
