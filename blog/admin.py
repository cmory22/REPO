from django.contrib import admin
from .models import Novinky



class NovinkyAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'date')



admin.site.register(Novinky, NovinkyAdmin)