from django.contrib import admin
from App1.models import Emp
class EmpAdmin(admin.ModelAdmin):
	ls = ['id','num','name','salary','address']

admin.site.register(Emp,EmpAdmin)