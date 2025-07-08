from django.contrib import admin
from .models import Artwork

# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('tag', 'created_at')
    list_filter = ('tag', 'created_at')
    ordering = ('-created_at',)