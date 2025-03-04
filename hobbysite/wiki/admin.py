from django.contrib import admin

from .models import Article, ArticleCategory

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory

    list_display = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = ('title', 'created_on', 'updated_on')


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)