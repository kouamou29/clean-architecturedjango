from django.contrib import admin

# Register your models here.
from.models import User, Category, Post


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)