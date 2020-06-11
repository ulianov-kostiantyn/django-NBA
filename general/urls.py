from django.urls import path
from . import views

app_name = 'general'

urlpatterns = [
    path('', views.TeamsListView.as_view(), name='all'),
    path('playes/<slug>/', views.PlayersListView.as_view(), name='team'),
    path('team/<slug>/', views.TeamDetailView.as_view(), name='detailteam' ),


]
