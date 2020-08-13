from django.urls import path
from django.urls import reverse
from . import views



app_name = 'usersactivity'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('signup', views.sign_up, name='sign_up'),
    path('profile', views.user_profile, name='profile'),
    path('logout', views.user_logout, name='logout'),
    path('change_password', views.change_user_password, name='change_password'),
    path('<int:pk>', views.ProfileUpdate.as_view(), name='profile_update'),


]

