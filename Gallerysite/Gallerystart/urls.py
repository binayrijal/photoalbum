from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,UserPasswordResetForm,MySetPasswordForm


urlpatterns = [
    path('',views.home,name='home'),
    path('album',views.album,name='album'),
    path('album/<slug:data>',views.showcategoryalbum,name='showalbum'),

    path('deletephoto/<int:id>',views.deletephoto,name="deletephoto"),
    path('logout/',auth_views.LogoutView.as_view(next_page='loginuser'),name='logout'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='Gallerystart/login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='Gallerystart/password-reset.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='Gallerystart/password-reset-done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Gallerystart/password-reset-confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Gallerystart/password-reset-complete.html'),name='password_reset_complete'),

]