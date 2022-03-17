from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category,Post,UserModel



class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name',)

admin.site.register(Category, CategoryAdmin)



class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'created_at')

admin.site.register(Post, PostAdmin)



class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email','born_date')

admin.site.register(UserModel, UserModelAdmin)



