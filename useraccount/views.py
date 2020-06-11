from .serializers import UserSerializer
import ast
from .decorators import serialize_exceptions
from django.shortcuts import render
#from .factories import create_user_profile_interactor,get_user_profile_interactor,update_user_profile_interactor


#def home(request):
   # return(render(request,'basis.html'))

class UserView(object):
#create_user_account_interactor_factory.get(),get_user_account_interactor_factory.get(),update_user_account_interactor_factory.get(),delete_user_account_interactor_factory.get()
    def __init__(self,get_user_account_interactor=None,create_user_account_interactor=None,update_user_account_interactor=None,delete_user_account_interactor=None):
        self.create_user_account_interactor = create_user_account_interactor
        self.get_user_account_interactor = get_user_account_interactor
        self.update_user_account_interactor = update_user_account_interactor
        self.delete_user_account_interactor = delete_user_account_interactor
    

    #Retrieve user viewfunction
    def get(self,id):
        user = self.get_user_account_interactor.set_params(id = id).execute()

        body = UserSerializer.serialize(user)
        status = 200

        return body, status


    def patch(self, user_id,firstname,lastname,college_name,email,department,skills,username):
        user = self.update_user_account_interactor.set_params(id=id,firstname=firstname,lastname=lastname,college_name=college_name,email=email,department=department,skills=skills,username=username).execute()
        body = UserSerializer.serialize(user)
        status = 200
        return body, status
    

    #Create user viewfunction
    def post(self, user_id,firstname,lastname,college_name,email,department,skills,username):
        user = self.create_user_account_interactor.set_params(user_id=user_id,firstname=firstname,lastname=lastname,college_name=college_name,email=email,department=department,skills=skills,username=username).execute()

        body = UserSerializer.serialize(user)
        status = 200
        return body, status


    def delete(self, user_id):
        self.delete_user_account_interactor.set_params(user_id=user_id).execute()

        body = None
        status = 200
        return body, status
    
