import itertools

from django.db import models


class Places(models.Model):
    town = models.TextField(max_length=50)
    country = models.TextField(max_length=40)  # This field type is a guess.

    def __str__(self):
        return self.town + ', ' + self.country


class Names(models.Model):
    name = models.TextField(max_length=100)
    date = models.IntegerField()
    place = models.ForeignKey(Places, on_delete=models.DO_NOTHING)
    email = models.TextField(max_length=50)

    def get_lang(self):
        lang = LanguagesToNames.objects.select_related('language')\
                                        .filter(name_id=self)
        return lang

    def get_prof(self):
        prof = ProfessionsToNames.objects.select_related('profession')\
                                        .filter(name_id=self)
        return prof

    def get_party(self):
        party = PartiesToNames.objects.select_related('party')\
                                        .filter(name_id=self)
        return party

    def __str__(self):
        return self.name


class Parties(models.Model):
    party = models.TextField(max_length=50)

    def __str__(self):
        return self.party


class Professions(models.Model):
    profession = models.TextField(max_length=50)

    def __str__(self):
        return self.profession


class Languages(models.Model):
    language = models.TextField(max_length=50)

    def __str__(self):
        return self.language


class LanguagesToNames(models.Model):
    name = models.ForeignKey(Names, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Languages, related_name='lang', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.language)


class PartiesToNames(models.Model):
    name = models.ForeignKey(Names, on_delete=models.DO_NOTHING)
    party = models.ForeignKey(Parties, related_name='part', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class ProfessionsToNames(models.Model):
    name = models.ForeignKey(Names, on_delete=models.DO_NOTHING)
    profession = models.ForeignKey(Professions, related_name='prof', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.profession
