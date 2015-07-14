from django.contrib import admin
from simba.models import UserProfile, Course


# Add in this class to customized the Admin Interface
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Course, CourseAdmin)
admin.site.register(UserProfile)

# Register your models here.
