from django.urls import path
from . import views
from .views import MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
   
  path('', views.index, name='index'),
  path('menu/', views.MenuItemView.as_view()),
  path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
  
]