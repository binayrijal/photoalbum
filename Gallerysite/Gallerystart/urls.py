from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('album',views.album,name='album'),
    path('album/<slug:data>',views.showcategoryalbum,name='showalbum')

]