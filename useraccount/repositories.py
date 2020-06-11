from .entities import User
from .exceptions import EntityDoesNotExistException
#from .conf import settings
from .models import ORMUser

#export DJANGO_SETTINGS_MODULE=sso.settings

class UserRepo(object):

    
    
    def _decode_db_user(self, db_user):

        return User(id=db_user.id,firstname=db_user.firstname, lastname=db_user.lastname,college_name=db_user.college_name, email=db_user.email,department=db_user.department,skills=db_user.skills,userimage=db_user.userimage,username=db_user.username)



    def create_user(self,id,username,firstname,lastname,college_name,email,department,skills):
        db_user = ORMUser.objects.create(id=id,username=username,firstname=firstname,lastname=lastname,college_name=college_name,email=email,department=department,skills=skills)
        

        return self._decode_db_user(db_user)

    

    def get_user(self, id):
        #try:
        db_user = ORMUser.objects.get(id=id)
        return self._decode_db_user(db_user)

        #except ORMUser.DoesNotExist:
            #raise EntityDoesNotExistException
    
    
    def update_user(self, user):

        orm_user = ORMUser.objects.get(id = user.id)

        orm_user.firstname = user.firstname
        orm_user.lastname = user.lastname
        orm_user.college_name = user.college_name
        orm_user.email = user.email
        orm_user.department = user.department
        orm_user.skills = user.skills
        orm_user.userimage = user.userimage
        orm_user.username = user.username
        orm_user.save()

        return self._decode_db_user(orm_user)


    def delete_user(self, id):
        orm_user = ORMUser.objects.filter(id=id)
        orm_user.delete()
        

        
#print(UserRepo.create_user(1,'ujjwww'))
