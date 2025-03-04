from django.contrib import admin
from .models import PostCategory, Post

class PostInline(admin.TabularInline):
    model = Post

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    inlines = [PostInline,]

class PostAdmin(admin.ModelAdmin):
    model = Post

# Register your models here.
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)