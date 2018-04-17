from django.shortcuts import render, redirect, HttpResponse
import random 
import time  

# Create your views here.
def index(request):
    if 'player_gold' not in request.session:
        request.session['player_gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    print(request.session['activity'])
    context = {
        'activity': request.session['activity'],
        'player_gold': request.session['player_gold']
    }

    return render(request, "first_app/index.html", context)
def reset(request):
    request.session.clear()
    return redirect('/')
def process_money(request):
    if request.method == "POST":
        value = request.POST['building']
        print(value)
        if value == 'farm':
            goldoutput = random.randint(10,20)
            request.session['player_gold'] += goldoutput
            activity = "<p class='gold'>You earned {} golds from the farm {}pm".format(goldoutput, time.strftime("%I:%M") + "</p>")
            request.session['activity'].append(activity)
            color = 'green'
            print(activity)
        if value == 'cave':
            goldoutput = random.randint(5,10)
            request.session['player_gold'] += goldoutput
            activity = "<p class='gold'>You earned {} golds from the farm {}pm".format(goldoutput, time.strftime("%I:%M") + "</p>")
            request.session['activity'].append(activity)
            color = 'green'
            print(activity)
        if value == 'house':
            goldoutput = random.randint(2,5)
            request.session['player_gold'] += goldoutput
            activity = "<p class='gold'>You earned {} golds from the farm {}pm".format(goldoutput, time.strftime("%I:%M") + "</p>")
            request.session['activity'].append(activity)
            color = 'green'
            print(activity)
        if value == 'casino':
            goldoutput = random.randint(-50,50)
            request.session['player_gold'] += goldoutput
            if goldoutput > 0:
                activity = "<p class='gold'>You earned {} golds from the farm {}pm".format(goldoutput, time.strftime("%I:%M") + "</p>")
                color = 'green'
            if goldoutput < 0:
                activity = "<p class='red'>You lost {} golds from the farm ...ouch!{}am".format(goldoutput, time.strftime("%I:%M") + "</p>")
                color = 'red'
            request.session['activity'].append(activity)
            print(activity)
        return redirect('/')

