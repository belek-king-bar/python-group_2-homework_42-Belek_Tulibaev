from django.contrib import admin
from webapp.models import User, Article, Comment, Rating

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('favorites',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)