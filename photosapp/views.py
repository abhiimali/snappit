from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Category , Photo
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = { 'categories' : categories ,'photos':photos}
    # photos = {'photos':photos}
    return render(request,'photos/gallery.html' , context=context)

def viewPhoto(request,pk):
    
    return render(request,'photos/photo.html')

def addPhoto(request):
    return render(request,'photos/addPhoto.html')