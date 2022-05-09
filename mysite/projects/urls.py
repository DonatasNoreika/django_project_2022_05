
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name="projects"),
    path('<int:pk>', views.ProjectDetailView.as_view(), name="project"),
    path('register/', views.register, name='register'),
    path('user_projects/', views.UserProjectListView.as_view(), name='user_projects'),
    path('new_project/', views.ProjectCreateView.as_view(), name='new_project'),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project_delete'),
]