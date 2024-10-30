from django.contrib import admin
from missions.models import Mission, Target

# Register your models here.

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('cat', 'is_complete')
    search_fields = ('cat__name',)
    list_filter = ('is_complete',)

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'mission', 'is_complete')
    search_fields = ('name', 'country')
    list_filter = ('is_complete', 'mission')
