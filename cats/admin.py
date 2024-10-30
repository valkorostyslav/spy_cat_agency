from django.contrib import admin

from cats.models import Cat

# Register your models here.

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'years_of_experience', 'breed', 'salary')
    search_fields = ('name', 'breed')
    list_filter = ('breed',)
