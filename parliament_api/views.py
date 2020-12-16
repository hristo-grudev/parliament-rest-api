from django.contrib.auth.models import User
from rest_framework import generics, viewsets
import django_filters.rest_framework

from .models import Names
from .serializer import ParSerializer, UserSerializer


class ParListApiView(generics.ListAPIView):
	queryset = Names.objects.all()
	serializer_class = ParSerializer
	filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
	filterset_fields = ['name', 'date', 'place', 'party']

	def list(self, request, *args, **kwargs):
		print(request.user)
		return super().list(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
