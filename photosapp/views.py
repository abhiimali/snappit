from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

from .models import Category , Photo
def gallery(request):
    category = request.GET.get('category')
    if category ==  None :
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
                 
    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = { 'categories' : categories ,'photos':photos}
    # photos = {'photos':photos}
    return render(request,'photos/gallery.html' , context=context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    
    return render(request,'photos/photo.html' ,{'photo':photo})

def addPhoto(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category = Category.objects.get_or_create(name=data['category_new']) 
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image=image
        ) 
        return redirect('/')
    context = { 'categories' : categories ,'photos':photos}
    return render(request,'photos/addPhoto.html',context)