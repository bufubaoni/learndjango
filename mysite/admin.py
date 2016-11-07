from django.contrib import admin
from .models import MyModel, somework, Category,MyAdmin

# Register your models here.
admin.site.register(MyModel)
admin.site.register(somework)
admin.site.register(Category)
# admin.site.register(MyAdmin)
