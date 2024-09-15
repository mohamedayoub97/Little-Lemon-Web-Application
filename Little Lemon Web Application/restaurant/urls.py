#define URL route for index() view
from django.urls import path
from django.contrib import admin

from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name="menu-items"),  # name for reverse() in tests
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
