from django.urls import path
from .views import  dashboard, Register, Login, logoutuser, profile_list, profile


app_name = 'dwitter'

urlpatterns = [
    
    path('register/', Register, name="register-page"),
    path('', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path("dashboard/", dashboard, name="dashboard"),
    path('profile_list/', profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]