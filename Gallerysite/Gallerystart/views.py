from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Albumform
from .models import Album
from django.db.models import Q
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def album(request):
    user=request.user
    albums=Album.objects.filter(user=user)
    return render(request,'Gallerystart/album.html',{'albums':albums})

@login_required
def showcategoryalbum(request,data=None):
    albums=None
    user=request.user
    if data in ["dashain","tihar","picnic"]:

        albums=Album.objects.filter(Q(classification=data)|Q(user=user))

    
    elif data == "others":
        
        albums=Album.objects.filter(Q(classification="") | Q(classification=data))
    else:
        albums=Album.objects.all()

    return render(request,'Gallerystart/album.html',{'albums':albums,'data':data})
    
@login_required
def deletephoto(request,id=None):
    if id:
        albums=Album.objects.get(id=id)
        albums.delete()
    return redirect ('album')
        
def login(request):
 return render(request, 'Gallery/login.html')



def customerregistration(request):
 if request.method=="POST":
  form=UserRegistrationForm(request.POST)
  if form.is_valid():
     form.save()
     messages.success(request,'congratulations!!Registration successfull')
     form=UserRegistrationForm()
     
 else:
  form=UserRegistrationForm()

 return render(request, 'Gallerystart/customerregistration.html',{
  'form':form,
 })