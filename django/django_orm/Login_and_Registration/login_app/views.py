from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
def index(request):

    return render(request, 'index.html')


def new_register(request): 
    errors = Register.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else : 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        context = {'first_name': first_name}

        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        Register.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
        return render(request, 'index2.html', context)
    
def validate_login(request):
    errors = Register.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else : return render(request, 'index2.html')



    # user = Register.objects.get(email=request.POST['email'])  
    # if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
    #     print("password match")
    # else:
    #     print("failed password")




def login(request):
    user = Register.objects.filter(email=request.POST['emaill'])
    if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['passwordd'].encode(),logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return render(request, 'index2.html')
        else:
            messages.error(request, 'Incorrect password. Please try again.')
    else:
        messages.error(request, 'Email not found. Please check your email and try again.', extra_tags='login_error')
    return redirect('/')


def logout(request):
    del request.session['userid'] 
    return redirect('/')


    

    
















