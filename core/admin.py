from django.contrib import admin
from .models import Profil, MediaContent

# Register your models here.
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    pass
    
@admin.register(MediaContent)
class MediaContent(admin.ModelAdmin):
    pass
