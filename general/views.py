from django.shortcuts import render
from django.views import generic
from general.models import Team, Player


class TeamsListView (generic.ListView):
    model = Team

class PlayersListView (generic.ListView):
    model = Player

class TeamDetailView(generic.DetailView):
    model = Team
