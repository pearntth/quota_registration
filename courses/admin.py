from django.contrib import admin
from .models import Course, QuotaRequest

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'semester', 'year', 'seats_available', 'is_open')
    list_filter = ('semester', 'year', 'is_open')
    search_fields = ('code', 'name', 'semester', 'year')
    list_editable = ('seats_available', 'is_open')

class QuotaRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'is_approved')

admin.site.register(Course, CourseAdmin)
admin.site.register(QuotaRequest, QuotaRequestAdmin)