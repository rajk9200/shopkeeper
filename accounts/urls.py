

from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('signup/',views.account_signup,name ='signup'),
    path('login/',views.account_login, name='login'),
    path('logout/',views.account_logout, name='logout'),
    path('profile/<str:email>/',views.account_profile, name='profile'),
    path('changepassword/<str:email>/',views.account_change_password,name='changepassword'),
]

