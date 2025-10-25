from django.contrib import admin
from .models import Link

# Register your models here.

# older way
# admin.site.register(Link)

# modern way
@admin.register(Link)
class LinkAdminModel(admin.ModelAdmin):
    list_display = ("name", "url")
    list_filters = ("name")