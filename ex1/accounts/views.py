from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        
        
        user=User.objects.create_user(firstname=firstname,lastname=lastname,username=username,email=email,password1=password1,password2=password2)
        user.save()
        print('user created')
        return redirect('/')
                
    else:
        return render(request,'register.html')
    
    # return render(request,'register.html')

# def returnback(request):
    
#     return redirect('/')