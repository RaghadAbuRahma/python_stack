from django.shortcuts import render, redirect

# app.secret_key = 'secret'

def counter(request):
    if 'count' not in request.session:
        request.session['count'] = 0 
    
    else : request.session['count'] = request.session['count'] +1 

    return render(request, 'index.html')


def destroySession(request):
    del request.session['count']	
    return redirect('/')

def reset(request):
    del request.session['count']
    return redirect('/')

# def userincrement(request):

def submitt(request):
    print(request.POST['incrementText'])
    request.session['count'] = request.session['count']+ int(request.POST['incrementText'])-1
    return redirect('/')








