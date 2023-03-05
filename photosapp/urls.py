from django.urls import path


from .views import gallery ,addPhoto ,viewPhoto 

urlpatterns = [
  
    path('',gallery,name="gallery"),
    path('photo/<str:pk>/',viewPhoto, name="photo"),
    path('add',addPhoto , name="add")

]
