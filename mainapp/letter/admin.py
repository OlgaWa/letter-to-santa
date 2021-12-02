from django.contrib import admin
from .models import ChristmasLetter


class LetterAdmin(admin.ModelAdmin):
    list_display = ['title', 'signature']


admin.site.register(ChristmasLetter, LetterAdmin)
