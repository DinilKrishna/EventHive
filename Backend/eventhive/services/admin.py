from django.contrib import admin
from .models import *

# Register your models here.

##superuser: admin@gmail.com
##pass: admin@123

admin.site.register(ServiceCategory)
admin.site.register(Venue)
admin.site.register(Catering)
admin.site.register(PhotographyVideography)
admin.site.register(Entertainment)
admin.site.register(EventPlanner    )
admin.site.register(Sports)
admin.site.register(ConcertAndShow)
admin.site.register(Hotel)
admin.site.register(SportsTicketType)
admin.site.register(ConcertTicketType)
admin.site.register(RoomType)