from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm


urlpatterns = [
    path('',views.home,name='home'),
    path('album',views.album,name='album'),
    path('album/<slug:data>',views.showcategoryalbum,name='showalbum'),

    path('deletephoto/<int:id>',views.deletephoto,name="deletephoto"),
    path('logout/',auth_views.LogoutView.as_view(next_page='loginuser'),name='logout'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='Gallerystart/login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('registration/', views.customerregistration, name='customerregistration'),

]