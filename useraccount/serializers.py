class ExceptionSerializer:

    @staticmethod
    def serialize(exception):
        return {
                   'error': {
                       'source': exception.source,
                       'code': exception.code,
                       'message': str(exception)
                    }
               }

class UserSerializer:

    @staticmethod
    def serialize(user):
        return {
                   'id': int(user.id),
                   'firstname':user.firstname,
                   'lastname': user.lastname,
                   'college_name': user.college_name,
                   'email': user.email,
                   'department': user.department,
                   'skills': user.skills,
                   'username':user.username,
                   'is_registered': user.is_registered,
                   'is_email_verified': user.is_email_verified,
               }