from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index_login'),
    # path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('cadastro/', views.register, name='register'),
    # path('usuarios/', views.users, name='users'),
]