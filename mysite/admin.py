from django.contrib import admin
from .models import MyModel, somework, Category

# Register your models here.
admin.site.register(MyModel)
admin.site.register(somework)
admin.site.register(Category)
