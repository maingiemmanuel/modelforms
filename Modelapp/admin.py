from django.contrib import admin
from .models import Students, Teachers, Parents, Courses, Posts

# Register your models here.
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Parents)
admin.site.register(Courses)
admin.site.register(Posts)