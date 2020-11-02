from django.shortcuts import render
from django.contrib.auth import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from groups.models import Group, GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.edit.CreateView):
     fields = ('name', 'description')
     model = Group

class SignleGroup(generic.edit.DetailView):
    model = Group

class ListGroups(generic.edit.DetailView):
    model = Group
