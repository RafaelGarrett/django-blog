from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.listarPosts, name='listar'),
    path('posts/novo', views.criarPost, name='novo'),
    path('posts/<int:id>', views.editarPost, name='editar'),
    path('posts/delete/<int:id>', views.deletarPost, name='deletar')
]