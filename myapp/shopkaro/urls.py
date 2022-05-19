from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.my_login, name='login'),
    path("register/", views.myregister.as_view(), name='myregister'),
    # path("register/", views.myregister, name='myregister'),

]
