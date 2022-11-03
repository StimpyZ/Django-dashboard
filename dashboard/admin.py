from django.contrib import admin
from .models import Elementos, Elementos1, Elementos2
from django.contrib.auth.models import Group

admin.site.site_header = 'DashboardAdmin'

class ElementoAdmin(admin.ModelAdmin):
  list_display = ('Year', 'Categoria', 'Cantidad')

# Register your models here.
admin.site.register(Elementos, ElementoAdmin)

admin.site.register(Elementos1, ElementoAdmin)

admin.site.register(Elementos2, ElementoAdmin)
# admin.site.unregister(Group)



