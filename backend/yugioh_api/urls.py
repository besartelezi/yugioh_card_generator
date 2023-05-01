from django.urls import include, re_path
from .views import (
    MonsterCardListApiView,
    MonsterCardDetailApiView
)

urlpatterns = [
    re_path('api', MonsterCardListApiView.as_view()),
    # try {card_id} after adding test
    re_path('api/<int:card_id>/', MonsterCardDetailApiView.as_view)
]
