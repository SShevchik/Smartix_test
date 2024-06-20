from rest_framework.exceptions import APIException


class AddressValidationException(APIException):
    status_code = 400
    default_detail = 'Invalid address'

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.status_code
        super().__init__(detail, code)
