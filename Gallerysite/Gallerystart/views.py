from django.shortcuts import render
from django.http import HttpResponse
from .forms import Albumform
from .models import Album

# Create your views here.
def home(request):
    if request.method=="POST":
        form=Albumform(request.POST,request.FILES)
        if form.is_valid():
            album=form.save(commit=False)
            album.user_id=request.user.id
            album.save()
    form=Albumform()
    return render(request,'Gallerystart/home.html',{'form':form})


def album(request):
    user=request.user
    albums=Album.objects.filter(user=user)
    return render(request,'Gallerystart/album.html',{'albums':albums})