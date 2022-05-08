from django.contrib import admin

from paSSengersformes.models import passengers

# Register your models here.


admin.site.register(passengers,admin.ModelAdmin)