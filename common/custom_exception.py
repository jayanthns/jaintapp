from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class IncorrectData(APIException):
    status_code = 400
    default_detail = 'Wrong format data, try again later.'
    default_code = 'bad_request'

class AuthFailed(APIException):
    status_code = 401
    default_detail = 'Incorrect authentication credentials.'
    default_code = 'authentication_failed'