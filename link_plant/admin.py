from django.contrib import admin
from link_plant.models import Profile, LinkP
# Register your models here.

admin.site.register(LinkP)
admin.site.register(Profile)  

# @admin.register(Link)
# class LinkAdminModel(admin.ModelAdmin):
#     list_display=("name", "slug")
#     list_filters= ("name")