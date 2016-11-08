from django.contrib import admin
from .models import MyModel, somework,menu_item
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
admin.site.register(MyModel)
admin.site.register(somework)
admin.site.register(menu_item,DraggableMPTTAdmin)

