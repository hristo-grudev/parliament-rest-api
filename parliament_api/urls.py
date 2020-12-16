from django.urls import path
from rest_framework.documentation import include_docs_urls

from .views import ParListApiView

urlpatterns = (
	path('', ParListApiView.as_view(), name='parliament list api'),
	path('docs/', include_docs_urls(title='My API title', public=False)),

)
