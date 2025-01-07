from django.urls import path, include
from . import views
from rest_framework.authtoken import views as rest_views


urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", rest_views.obtain_auth_token, name="signin") # authorizes and returns token
]