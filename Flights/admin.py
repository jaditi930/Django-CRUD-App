from django.contrib import admin
from .models import Flights
# Register your models here.
# admin.site.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display=("id","start_point","dest")
admin.site.register(Flights,FlightsAdmin)