from django.contrib import admin
from django.urls import path, include
from management_api.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include('management_api.urls')),  # Ensure this is correct
]
