from django.urls import path
from .views import character_list, characters_by_universe, characters_by_ability, character_create, character_delete

urlpatterns = [
    path('', character_list, name='character_list'),
    path('universe/<int:universe_id>/', characters_by_universe, name='characters_by_universe'),
    path('ability/<int:ability_id>/', characters_by_ability, name='characters_by_ability'), 
    path('create/', character_create, name='character_create'),
    path('delete/<int:pk>/', character_delete, name='character_delete'),
]