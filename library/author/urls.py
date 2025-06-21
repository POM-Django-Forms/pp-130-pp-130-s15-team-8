from django.urls import path
from . import views


urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('create/', views.author_create, name='author_create'),
    path('delete/<int:author_id>/', views.author_delete, name='author_delete'),
]