from django.contrib import admin

from .models import Article, ArticleCategory

class ArticleAdminInline(admin.TabularInline):
    model = Article
    readonly_fields = ['created_on', 'updated_on']

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleAdminInline]

    list_display = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = ('title', 'created_on', 'updated_on')


admin.site.register(ArticleCategory, ArticleCategoryAdmin)