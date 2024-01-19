from django.contrib import admin
from car_app.models import Car,Comment,Order,Job_seeker

# Register your models here.
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Job_seeker)