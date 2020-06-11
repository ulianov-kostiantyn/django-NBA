from django.urls import path
from . import views

app_name = 'general'

urlpatterns = [
    path('', views.TeamsListView.as_view(), name='all'),
    path('players/', views.PlayersListView.as_view(), name='team'),
    path('team/<slug>/', views.TeamDetailView.as_view(), name='detailteam' ),
    path('player/<slug>/', views.PlayerDetailView.as_view(), name='detailplayer' ),


]
