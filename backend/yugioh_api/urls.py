from django.contrib import admin
from django.urls import path, include
from yugioh_api import urls as yugioh_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('yugioh_cards/', include(yugioh_urls))
]
