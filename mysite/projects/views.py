from django.shortcuts import render
from django.views import generic
from .models import Project


# Create your views here.
class ProjectListView(generic.ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'project'
