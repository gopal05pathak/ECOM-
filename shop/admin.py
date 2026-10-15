from django.contrib import admin

# Register your models here.
# hum shop ke admin mein hai kyuki hume isi ke model ko register krna hai

# this is how we register models
from .models import Product , Contact , Orders , OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)