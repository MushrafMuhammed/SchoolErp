from django.urls import path
from . import views
urlpatterns = [
    path("login", views.login_fun, name="admin_login"),
    
    # path("home", views.home_fun, name="home"),

]