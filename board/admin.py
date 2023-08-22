from django.contrib import admin
from .models import Category, College, Major, Number, User, Challenge
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class CollegeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(College, CollegeAdmin)

class MajorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Major, MajorAdmin)

admin.site.register(Number)

admin.site.register(User)

admin.site.register(Challenge)