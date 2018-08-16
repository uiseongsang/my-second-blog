from django.contrib import admin
from .models import Post

class AuthorAdumin(admin.ModelAdmin):
    pass

admin.site.register(Post)
