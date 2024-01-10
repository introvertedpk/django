from django.shortcuts import render
from .models import destination
# Create your views here.

def index(request):
    
    dest1=destination()
    dest1.id=1
    dest1.name='Mumbai'
    dest1.desc='It is a good place to live'
    dest1.img='destination_1.jpg'
    dest1.price=700
    dest1.offer=True
    
    dest2=destination()
    dest2.id=2
    dest2.name='Chennai'
    dest2.desc='Namma Chennai'
    dest2.img='destination_2.jpg'
    dest2.price=600
    dest2.offer=False
    
    dest3=destination()
    dest3.id=3
    dest3.name="Banglore"
    dest3.img='destination_3.jpg'
    dest3.desc="Namaskaram Bengaluru"
    dest3.price=600
    dest3.offer=True
    
    dests=[dest1,dest2,dest3]
    
    return render(request,'index.html',{'dests':dests})