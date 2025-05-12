from django.contrib import admin
from .models import Course,Category

admin.AdminSite.site_header = "Courses Admin"
admin.AdminSite.site_title = "My Courses"
admin.AdminSite.index_title = "Welcome to the Courses admin area"

class CoursesInline(admin.TabularInline):
    model=Course
    exclude=['created_at']
    extra=1
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['created_at'], 'classes': ['collapse']})
    ]
    inlines=[CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
