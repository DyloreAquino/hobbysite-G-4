from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline,]


class ArticleAdmin(admin.ModelAdmin):
    model = Article


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
