class UserValidator:

    USERNAME_MIN_LENGTH = 6
    USERNAME_MAX_LENGTH = 20
    USERNAME_REGEX = '(?!\.)(?!\_)(?!.*?\.\.)(?!.*?\.\_)(?!.*?\_\.)(?!.*?\_\_)(?!.*\.$)(?!.*\_$)[a-z0-9_.]+$'

    def __init__(self, forbidden_email_domains, user_repo):

    #def __init__(self, project_name, forbidden_usernames, forbidden_email_domains, user_repo):
        self.project_name = project_name
        # have to define these in seprate file self.forbidden_usernames = forbidden_usernames
        # have to define thse self.forbidden_email_domains = forbidden_email_domains
        self.user_repo = user_repo
# validator for user
    def validate(self, user):
        if len(user.username) < UserValidator.USERNAME_MIN_LENGTH or \
                len(user.username) > UserValidator.USERNAME_MAX_LENGTH:
            raise InvalidEntityException(source='username', code='wrong_size',
                                         message='Username length should be between 6 and 20 chars')
        if not re.match(UserValidator.USERNAME_REGEX, user.username):
            raise InvalidEntityException(source='username', code='not_allowed', message='Username not allowed')
        #if self.project_name in user.username:
            #raise InvalidEntityException(source='username', code='not_allowed', message='Username not allowed')
        if user.username in self.forbidden_usernames:
            raise InvalidEntityException(source='username', code='not_allowed', message='Username not allowed')
        try:
            self.user_repo.get_user(username=user.username)
            raise InvalidEntityException(source='username', code='not_allowed', message='Username not allowed')
        except EntityDoesNotExistException:
            pass

        
        return True