from django.contrib import admin
from piServer.models import UserProfile, Alarm, Building, Outlet

admin.site.register(UserProfile)
admin.site.register(Alarm)
admin.site.register(Building)
admin.site.register(Outlet)
