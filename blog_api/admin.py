from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category,Post,Comment,UserModel



class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name',)
admin.site.register(Category, CategoryAdmin)



class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author','category','created_at')
admin.site.register(Post, PostAdmin)



class CommentAdmin(admin.ModelAdmin):
   list_display = ('comment_by','post', 'created_at',)
admin.site.register(Comment, CommentAdmin)



class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email','born_date',)
admin.site.register(UserModel, UserModelAdmin)



