from django.contrib import admin
from .Souvenir.souvenir_models import Bread, Shop, ShopLocation
# Register your models here.
admin.site.register(Bread)
admin.site.register(Shop)
admin.site.register(ShopLocation)
