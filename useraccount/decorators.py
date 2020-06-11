from .serializers import ExceptionSerializer
from .exceptions import UserException,InvalidEntityException,ConflictException,EntityDoesNotExistException

exception_status_code_mapper = {
        InvalidEntityException: 422,
        EntityDoesNotExistException: 404,
        ConflictException: 409,
        #NoLoggedException: 401,
      
        }
        
def serialize_exceptions(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserException as e:
            body = ExceptionSerializer.serialize(e)
            status = exception_status_code_mapper[type(e)]
        return body, status
    return func_wrapper