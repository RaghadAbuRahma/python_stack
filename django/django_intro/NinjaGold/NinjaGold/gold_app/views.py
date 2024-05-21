from django.shortcuts import render, redirect
import random
def index(request):
    if 'count' not in request.session: 
        request.session['count'] = 0  
    context = {'count': request.session['count']}
    return render(request, 'index.html', context)


def processMoney(request):
    


    if request.POST.get('which_form') :
        randumNum = random.randint(10, 20)
        request.session['count'] += randumNum
        place = request.POST.get('which_form')
        request.session['message'] = f'You entered a {place} and earned {randumNum} gold .' 

    return redirect('/')




def quest(request):
    if request.POST.get('which_form') == 'Quest': 

        if 'count' not in request.session: 
            request.session['count'] = 0  
        randumNum = random.randint(-50, 50)
        request.session['count'] += randumNum 
        place = request.POST.get('which_form') == 'Quest'
        if randumNum > 0 :
            request.session['message'] = f'You entered a {str(place)} and earned {randumNum} gold .' 
        if randumNum < 0 :
            request.session['message'] = f'You entered a {str(place)} and lost {randumNum} gold .' 

        return redirect('/')

def clear(request):
    # for 'count' in request.session:
    del request.session['count']
    return redirect('/')





    



    
    
    



    





