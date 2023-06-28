from django.urls import path, include
from . import views

urlpatterns = [
    path('developer/', views.getUsers),
    path('developer/<int:id>', views.getUser),
    path('developer/<int:id>', views.deleteUser),
    path('developer/', views.updateUser),
    path('developer/', views.createUser),
    path('project/', views.getProjects),
    path('project/', views.createProject),
    path('project/', views.updateProject),
    path('project/<int:id>', views.getProjects),
    path('project/<int:id>', views.deleteProject),
    path('task/', views.getUsers),
    path('task/<int:id>', views.getUser),
    path('task/<int:id>', views.deleteUser),
    path('task/', views.updateUser),
    path('task/', views.createUser),
    path('bug/', views.getBugs),
    path('bug/', views.createBug),
    path('bug/', views.updateBug),
    path('bug/<int:id>', views.getBugs),
    path('bug/<int:id>', views.deleteBug),
]