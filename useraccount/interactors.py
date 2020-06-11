from .entities import User
#from .exceptions import EntityDoesNotExistException, InvalidEntityException


class GetUserAccountInteractor(object):

    def __init__(self, user_repo):
        #self.user_validator = user_validator
        self.user_repo = user_repo
        

    def set_params(self,id):
        self.id = id
        #self.username = username
        #self.email = email
        return self

    def execute(self):
        #user = self.user_repo.get_user(id=self.user_id,username=self.username,email=self.email)
        #fetched_user = User(user_id=user.user_id,username=self.username, email=self.email, is_email_verified=False)

        return self.user_repo.get_user(id=self.id)
 
class UpdateUserAccountInteractor(object):

    def __init__(self, user_repo):

        self.user_repo = user_repo
        

    def set_params(self,id,firstname,lastname,college_name, email,department,skills,userimage,username,**kwargs):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.college_name = college_name
        self.email = email
        self.department = department
        self.skills = skills
        self.userimage = userimage
        self.username = username

        return self


    def execute(self):

        user = self.user_repo.get_user(id=self.id)

        updated_firstname = self.firstname if self.firstname is not None else user.first_name
        updated_lastname = self.lastname if self.lastname is not None else user.last_name
        updated_college_name = self.college_name if self.college_name is not None else user.college_name
        updated_email = self.email if self.email is not None else user.email
        updated_department = self.department if self.department is not None else user.department
        updated_skills = self.skills if self.skills is not None else user.skills
        updated_username = self.username if self.username is not None else user.username

        updated_user = User(self.id,updated_firstname,updated_lastname,updated_college_name,updated_email,updated_department,updated_department,updated_skills,updated_username)  
        #confirmation_token interactor will be written here
        return self.user_repo.update_user(updated_user)
class CreateUserAccountInteractor(object):
#can add user_validator as second argument
    def __init__(self, user_repo):

        #self.user_validator = user_validator
        self.user_repo = user_repo
        

    def set_params(self,id,username,firstname,lastname,college_name,email,department,skills):
        self.id = id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.college_name = college_name
        self.email = email
        self.department= department
        self.skills=skills

        #otherfields
        return self

    def execute(self):
        user = self.user_repo.create_user(id=self.id,username=self.username,firstname=self.firstname,lastname=self.lastname,college_name=self.college_name,email=self.email,department=self.department,skills=self.skills)
        return user
        

class DeleteUserAccountInteractor(object):
#can add user_validator as second argument
    def __init__(self, user_repo):
        self.user_repo = user_repo
        

    def set_params(self, id):
        self.id = id
    

    def execute(self):
    
       self.user_repo.delete_user(id=self.id)
       
#UpdateUserAccountInteractor(UserRepo)
#print()