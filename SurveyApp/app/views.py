from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm, RateForm
from .models import Poll, CreateUserForm, Rate
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request,'register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        user = request.user
        polls = Poll.objects.all()
        context = {'polls':polls}
        return render(request,'home.html',context)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'user or password is not correct!')
    context = {}
    return render(request,'login.html',context)

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        print("logged out succesfully")
    return redirect('login')

def home(request):
    polls = Poll.objects.all()
    context = {'polls':polls}
    return render(request,'home.html',context)

def ratehome(request):
    rates = Rate.objects.all()
    context = {'rates':rates}
    return render(request,'rateHome.html',context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {'form':form}
    return render(request,'create.html',context)

def createRating(request):
    if request.method == 'POST':
        form = RateForm(request.POST)       
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RateForm()
    context = {'form':form}
    return render(request,'createRate.html',context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected = request.POST['poll']
        if selected == 'option1':
            poll.option_count_one +=1
        elif selected == 'option2':
            poll.option_count_two +=1
        elif selected == 'option3':
            poll.option_count_three +=1
        elif selected == 'option4':
            poll.option_count_four +=1
        elif selected == 'option5':
            poll.option_count_five +=1
        else:
            return HttpResponse(400,'Invalid')
        poll.save()

        return redirect('result',poll_id)
    context = {'poll':poll}
    return render(request,'vote.html',context)

def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll':poll}
    return render(request,'result.html',context)