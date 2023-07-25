from django.contrib import admin

from apps.common.models import *

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Occupation)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
