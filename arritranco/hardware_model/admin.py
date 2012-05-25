from django.contrib import admin

from models import Manufacturer, HwModel, HwType, RackableModel

class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(HwModel)
admin.site.register(HwType)
admin.site.register(RackableModel)
