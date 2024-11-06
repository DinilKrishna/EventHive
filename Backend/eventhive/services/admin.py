from django.contrib import admin
from .models import ServiceCategory, Entertainment

# Register your models here.

##superuser: admin@gmail.com
##pass: admin@123

admin.site.register(ServiceCategory)
admin.site.register(Entertainment)