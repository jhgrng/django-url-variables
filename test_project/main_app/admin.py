from django.contrib import admin


# Register your models here.
from .models import Country, City, Street


class CountryAdmin(admin.ModelAdmin):
    class Meta:
        app_label = 'main_app'

    pass


class CityAdmin(admin.ModelAdmin):
    class Meta:
        app_label = 'main_app'

    pass


class StreetAdmin(admin.ModelAdmin):
    class Meta:
        app_label = 'main_app'

    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Street, StreetAdmin)
