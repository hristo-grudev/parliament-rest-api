from dataclasses import fields

from rest_framework import serializers, relations
from .models import Names, Places, Languages


class PlaceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Places
		fields = ('town', 'country')


class LanguageSerializer(serializers.ModelSerializer):

	class Meta:
		model = Languages
		fields = ('language', )


class ParSerializer(serializers.ModelSerializer):
	place = PlaceSerializer(many=False, read_only=True)
	language = LanguageSerializer(many=False, read_only=True)

	class Meta:
		model = Names
		fields = ('name', 'place', 'date', 'email', 'language')

