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
        return render(request, 'wall.html', context)
    
    
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
            request.session['user_name'] = logged_user.first_name
            massages = Massages.objects.all()
            comment = Comments.objects.all()
            context = {
            'massages': massages,
            'user': request.session['user_name'],
            'comment': comment
            }
            return render(request, 'wall.html', context)
        # if not request.session['userid']: 
        #     return redirect ('/')
        else:
            messages.error(request, 'Incorrect password. Please try again.')
    else:
        messages.error(request, 'Email not found. Please check your email and try again.', extra_tags='login_error')
    return redirect('/')


def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')


def post_massage(request):
    if request.method == 'POST':
        register = Register.objects.get(id=request.session['userid'])
        massage = request.POST['massage']
        Massages.objects.create(register=register, massage=massage)
        massages = Massages.objects.all()
    
    context = {
        'massages': massages,
        'user': request.session['user_name']
    }

    return render(request, 'wall.html', context)


def post_comment(request,id):

    massage = Massages.objects.get(id=id)
    register = Register.objects.get(id=request.session['userid'])
    comment = request.POST['comment']
    Comments.objects.create(user=register, massage=massage, comment=comment)

    massages = Massages.objects.all()
    comments = Comments.objects.all()
    # comment = Comments.objects.all()
    context = {
    'massages': massages,
    'user': request.session['user_name'],
    'comments': comments
    }
    return render(request, 'wall.html', context)

