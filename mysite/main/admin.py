from django.contrib import admin
from .models import logo,welcome,Content,text,price,contact
# Register your models here.

admin.site.register(logo)
admin.site.register(welcome)
admin.site.register(Content)
admin.site.register(text)
admin.site.register(price)

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
