  
from django.urls import path

from .views import GameDetails,GameList

urlpatterns = [
    path('', GameList.as_view(), name='games'),
    path('<int:pk>/', GameDetails.as_view(), name='game_details')
]