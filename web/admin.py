from django.contrib import admin
from .models import SkillList, MapBadge, MailBox, BucketList, FactItem, PfItem

# Register your models here.
class PfItemAdmin(admin.ModelAdmin):
    list_display = ['dfilter', 'year', 'month', 'name']

admin.site.register(PfItem, PfItemAdmin)

class FactItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'count']

admin.site.register(FactItem, FactItemAdmin)

class BucketListAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'year']

admin.site.register(BucketList, BucketListAdmin)

class MailBoxAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'memo', 'ip']

admin.site.register(MailBox, MailBoxAdmin)

class SkillListAdmin(admin.ModelAdmin):
    list_display = ['name', 'scale']
    list_editable = ['scale']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SkillList, SkillListAdmin)

class MapBadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']
    list_editable = ['year']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MapBadge, MapBadgeAdmin)

