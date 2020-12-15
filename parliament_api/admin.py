from django.contrib import admin

from .models import Names, Languages, Parties, Places, Professions, LanguagesToNames, ProfessionsToNames, PartiesToNames

admin.site.register(Names)
admin.site.register(Languages)
admin.site.register(Parties)
admin.site.register(Places)
admin.site.register(Professions)
admin.site.register(LanguagesToNames)
admin.site.register(ProfessionsToNames)
admin.site.register(PartiesToNames)
