from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_filter = ['reported']
    list_display = ['id', 'comment', 'date', 'movie', 'user', 'reported']

admin.site.register(Review, ReportAdmin)







