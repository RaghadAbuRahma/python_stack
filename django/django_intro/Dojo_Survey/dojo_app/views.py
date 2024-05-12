from django.shortcuts import render

def index(request):
    print('hi')
    return render(request, 'index.html')

def result(request):
    data = {
    "name" : request.POST['Name'],
    "location" : request.POST['location'],
    "lang" : request.POST['lang'],
    'comment': request.POST['comment'],
    }
    # print (data)
    return render(request, 'result.html', data)


    
    
    

