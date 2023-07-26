from django.contrib import admin

from apps.article.models import Occupation, Article, Tag, Category, \
    Author, Subscription, AuthorSocialMedia, Instagram

admin.site.register(Subscription)
admin.site.register(AuthorSocialMedia)
admin.site.register(Instagram)
admin.site.register(Occupation)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
