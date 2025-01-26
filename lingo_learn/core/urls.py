from django.urls import path, include
from . import views
from rest_framework.authtoken import views as rest_views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("signin/", rest_views.obtain_auth_token, name="signin"), # authorizes and returns token
    path("get-test/", views.get_test, name="getTest"),
    path("grade-test/", views.grade_test, name="gradeTest")
]