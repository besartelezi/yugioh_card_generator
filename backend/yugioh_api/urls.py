from django.urls import include, re_path
from .views import (
    MonsterCardListApiView,
)

urlpatterns = [
    re_path('api', MonsterCardListApiView.as_view())
]
