from app.exceptions import catchable


class InvalidCredentials(catchable):
    status_code = 401
    message = "invalid credential"
    