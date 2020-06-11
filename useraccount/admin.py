from django.contrib import admin

# Register your models here.
from useraccount.models import ORMProject,ORMUser,UserProfile,Department,Skill
admin.site.register(ORMProject)
admin.site.register(UserProfile)
admin.site.register(ORMUser)
admin.site.register(Department)
admin.site.register(Skill)




