from validator import Validator


class LoginForm(Validator):
    username = 'required'
    password = 'required'

    message = {
        'username': {
            'required': 'The email field is required',
        },
        'password': {
            'required': 'The password field is required',
            'password': 'The password should be greater then 7 characters with alpha and numeric.'
        },
    }
