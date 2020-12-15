from rest_framework import generics, mixins
import django_filters.rest_framework

from .models import Names, Languages
from .serializer import ParSerializer


class ParListApiView(generics.ListAPIView):
	queryset = Names.objects.all()
	serializer_class = ParSerializer
	filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
	filterset_fields = ['name', 'date', 'place', ]

	def list(self, request, *args, **kwargs):
		print(request.user)
		return super().list(request, *args, **kwargs)
