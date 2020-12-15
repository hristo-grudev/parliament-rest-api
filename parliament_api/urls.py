from django.urls import path

from .views import ParListApiView

urlpatterns = (
	path('', ParListApiView.as_view(), name='parliament list api'),
)
