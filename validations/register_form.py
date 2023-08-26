from validator import Validator


class RegisterForm(Validator):
    email = 'required|email|unique:AUTH_USER_MODEL,email'
    username = 'required|unique:AUTH_USER_MODEL,username'
    password = 'required|password:low'
    password_confirm = 'same:password'

    message = {
        'username': {
            'required': 'The username field is required',
            'unique': 'This username is already in use.'
        },
        'email': {
            'required': 'The email field is required',
            'email': 'The email must be a valid email address.',
            'unique': 'This email is already in use.'
        },
        'password': {
            'required': 'The password field is required',
            'password': 'The password should be greater then 7 characters with alpha and numeric.'
        },
        'password_confirm': {
            'same': 'The input value is not same as the value of password'
        }
    }
