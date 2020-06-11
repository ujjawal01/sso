class User:

    def __init__(self, id=None, firstname=None, lastname=None,college_name=None, email=None, is_email_verified=None,role=None,is_active=None,department=None,skills=None,userimage=None,username=None,password=None,disable_account=None,last_login=None,login_count=None):
        self._id = id
        self._firstname = firstname
        self._username = username
        self._lastname = lastname
        self._college_name = college_name
        self._email = email
        self._is_email_verified = is_email_verified
        self._role = role
        self._is_active = is_active
        #self._department = department
        self._skills = skills
        #self._userimage = userimage
        self._username = username
        #self._disable_account = disable_account
        self._last_login = last_login
        self._login_count = login_count

    @property
    def id(self):
        return self._id

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def college_name(self):
        return self._college_name

   
    @property
    def email(self):
        return self._email

    @property
    def is_email_verified(self):
        return self._is_email_verified

    @property
    def role(self):
        return self._role
    
    @property
    def is_active(self):
        return self._is_active
    
    @property
    def department(self):
        return self._department
    
    @property
    def skills(self):
        return self._skills
    
    @property
    def userimage(self):
        return self._userimage
    
    @property
    def username(self):
        return self._username
    
    @property
    def disable_account(self):
        return self._disable_account
    
    @property
    def last_login(self):
        return self._last_login


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

class Department:

    def __init__(self, id=None, name=None):
        self._id = id
        self._name = name

    @property
    def user_id(self):
        return self._id

    @property
    def name(self):
        return self._name

   
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

class UserProfile:


    def __init__(self, user=None,about_me=None, phone=None,projects=None):
        self._user = user
        self._about_me = about_me
        self._phone = phone
        self._projects = projects
        
        
    @property
    def user(self):
        return self._user

    @property
    def about_me(self):
        return self._about_me

    @property
    def phone(self):
        return self._phone

    @property
    def projects(self):
        return self._projects

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

class ORMProject:

    def __init__(self, id=None,project_name=None, project_description=None,technology=None):
        self._id = id
        self._project_name = project_name
        self._project_description = project_description
        self._technology = technology
        #self._user_id = user_id
        
    @property
    def id(self):
        return self._id

    @property
    def project_name(self):
        return self._project_name

    @property
    def project_description(self):
        return self._project_description

    @property
    def technology(self):
        return self._technology

   
   # @property
    #def user_id(self):
     #   return self._user_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other










    








    









    








    
