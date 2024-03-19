from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(ProfileModel)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)

class FormalModelAdmin(admin.ModelAdmin):
    list_display=['image','title','prize','description']
admin.site.register(FormalModel,FormalModelAdmin)

class TshirtsModelAdmin(admin.ModelAdmin):
    list_display=['image','title','prize','description']
admin.site.register(TshirtsModel,TshirtsModelAdmin)

class SuitsModelAdmin(admin.ModelAdmin):
    list_display=['image','title','prize','description']
admin.site.register(SuitsModel,SuitsModelAdmin)

class KurtasModelAdmin(admin.ModelAdmin):
    list_display=['image','title','prize','description']
admin.site.register(KurtasModel,KurtasModelAdmin)

class TopsModelAdmin(admin.ModelAdmin):
    list_display=['image','title','prize','description']
    # TopsModel('description')
admin.site.register(TopsModel,TopsModelAdmin)

