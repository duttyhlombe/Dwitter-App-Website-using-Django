from django.urls import path
from .views import HomePage, dashboard, Register, Login, logoutuser, profile_list, profile


app_name = 'dwitter'

urlpatterns = [
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path("dashboard/", dashboard, name="dashboard"),
    path('profile_list/', profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]