from django.contrib import admin
from .models import Article, ArticleCategory, Comment, ArticleImage


class ArticleImageAdmin(admin.ModelAdmin):
    model = ArticleImage


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleImageInline,]


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline,]


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleImage, ArticleImageAdmin)
admin.site.register(Comment, CommentAdmin)
