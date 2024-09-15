#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from restaurant import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

app_name = 'api'  # For tests

urlpatterns = [

   path('admin/', admin.site.urls),

   # TODO: Which?
   path('api/', include('restaurant.urls')),
#   path('restaurant/menu/', include('restaurant.urls')),
   path('restaurant/booking/', include(router.urls)),  # localhost:8000/restaurant/booking/tables

    # The following are valid endpoints automatically created by Djoser
    # auth/users/       [POST] to register a user with username, password, email
    # auth/users/me     [GET]  with token
    # auth/token/login  [POST] returns a bearer token for future API calls
    # auth/token/logout [POST] with token
    # jwt/create
    path('auth/', include('djoser.urls')),  # env\Lib\site-packages\djoser\urls
    path('auth/', include('djoser.urls.authtoken')),
]


