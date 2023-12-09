from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Albumform
from .models import Album
from django.db.models import Q

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

def showcategoryalbum(request,data=None):
    albums=None
    if data in ["dashain","tihar","picnic"]:

        albums=Album.objects.filter(classification=data)

    
    elif data == "others":
        
        albums=Album.objects.filter(Q(classification="") | Q(classification=data))
    else:
        albums=Album.objects.all()

    return render(request,'Gallerystart/album.html',{'albums':albums,'data':data})
    

def deletephoto(request,id=None):
    if id:
        albums=Album.objects.get(id=id)
        albums.delete()
    return redirect ('album')
        
    