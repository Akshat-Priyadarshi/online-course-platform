# Register your models here.
from django.contrib import admin
from .models import (
    Profile, Student, Instructor, Course, University,
    OnlineContent, CourseContent
)

# This allows you to edit the Profile (Role) directly on the User page
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'student_id', 'instructor_id')
    list_filter = ('role',)

admin.site.register(Profile, ProfileAdmin)

# Registering your existing schema tables so the Admin can manage them
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(University)

admin.site.register(OnlineContent)
admin.site.register(CourseContent)