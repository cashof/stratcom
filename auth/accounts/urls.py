from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.user_list, name='user-list'),
    path('create-user', views.create_user, name='user-create-user'),
    path('user-detail/<int:pk>/', views.user_detail, name='user-detail'),
    path('user-update/<int:pk>/', views.user_update, name='user_update'),
    path('user-delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('search-users', views.search_users, name='search_users'),

]   