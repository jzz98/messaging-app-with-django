from django.urls import path
from . import views

urlpatterns = [
    path('', views.singup, name="singup"),
    path('login/', views.login_view, name="login"),

]