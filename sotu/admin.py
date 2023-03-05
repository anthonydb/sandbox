from django.contrib import admin
from sotu.models import Speech


class SpeechAdmin(admin.ModelAdmin):
    list_display = ('president', 'title', 'speech_date')
    readonly_fields = ('search_speech_text',)

admin.site.register(Speech, SpeechAdmin)
