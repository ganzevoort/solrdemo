from django.contrib import admin
from .models import Country, Manufacturer, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 2


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    inlines = [CarModelInline]


admin.site.register(Country)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(CarModel)
