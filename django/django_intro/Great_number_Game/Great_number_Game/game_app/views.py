from django.shortcuts import render, redirect

def randomNum(request):
    import random  
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    return render(request, 'index.html')


def compare(request):
    guess = request.POST.get('guess')
    if guess is None:
        return render(request, 'index.html', {'error_message': 'Please provide a guess.'})
    
    guess = int(request.POST['guess'])
    number = int(request.session['number'])
    request.session['text']=""
    request.session['color']=""
    if guess > number:
        request.session['text']="too high"
        request.session['color']="red"
    elif guess < number:
        request.session['text']="too low"
        request.session['color']="red"
    else:
        request.session['text'] =  f"{request.session['number']} was the number!"
        request.session['color'] = "green"
    return redirect('/')
    






    
    


