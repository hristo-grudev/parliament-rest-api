from dataclasses import fields

from django.contrib.auth.models import User
from rest_framework import serializers, relations
from .models import Names, Places, Languages, LanguagesToNames, Professions, ProfessionsToNames, Parties, PartiesToNames


class PlaceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Places
		fields = ('town', 'country')


class NameLangSerializer(serializers.ModelSerializer):

	class Meta:
		model = Languages
		fields = ('language', )


class LanguageSerializer(serializers.ModelSerializer):
	language = NameLangSerializer(many=False, read_only=True)

	class Meta:
		model = LanguagesToNames
		fields = ('language', )


class NameProfSerializer(serializers.ModelSerializer):

	class Meta:
		model = Professions
		fields = ('profession', )


class ProfessionSerializer(serializers.ModelSerializer):
	profession = NameProfSerializer(many=False, read_only=True)

	class Meta:
		model = ProfessionsToNames
		fields = ('profession', )


class NamePartySerializer(serializers.ModelSerializer):

	class Meta:
		model = Parties
		fields = ('party', )


class PartySerializer(serializers.ModelSerializer):
	party = NamePartySerializer(many=False, read_only=True)

	class Meta:
		model = PartiesToNames
		fields = ('party', )


class ParSerializer(serializers.ModelSerializer):
	place = PlaceSerializer(many=False, read_only=True)
	lang = LanguageSerializer(many=True, source='get_lang', read_only=True)
	profession = ProfessionSerializer(many=True, source='get_prof', read_only=True, required=False)
	party = PartySerializer(many=True, source='get_party', read_only=True, required=False)

	class Meta:
		model = Names
		fields = ('name', 'place', 'date', 'email', 'lang', 'profession', 'party', )



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'