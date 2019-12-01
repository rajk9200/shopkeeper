from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm,ChangePassword
from .models import Accounts
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def dashboard(request):
    user_name = 'not_login'
    if not request.session.get('user_email', None):
        return redirect('login')
    else:
        email = request.session.get('user_email', None)
        user_name1 = Accounts.objects.filter(email = email)
        for i in user_name1:
            user_name=i.username
    context ={
        'user_name':user_name
    }
    return render(request,'dashbord.html',context)

def account_signup(request):



    form =SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request,'signup.html',context)

def account_login(request):
    if request.session.get('user_email', None):
        return redirect('dashboard')
    form =LoginForm(request.POST or None)
    if form.is_valid():
        email =form.cleaned_data.get('email')
        password =form.cleaned_data.get('password')
        user_auth = Accounts.objects.filter(email=email,password=password)
        if user_auth.exists():
            request.session['user_email'] = email
            return redirect('dashboard')
        else:
            messages.success(request, 'Email or Password Incorrect!')




    context = {
        'form': form
    }
    return render(request,'login.html',context)


def account_profile(request,email=None):

    account = Accounts.objects.get(username=email)

    context={
       'account':account,
    }
    return render(request,'profile.html',context)

def account_change_password(request,email=None):
    print(email,type(email))
    form =ChangePassword(request.POST or None)
    if form.is_valid():
        old_password =form.cleaned_data.get('old_password')
        password =form.cleaned_data.get('new_password')
        user_auth = Accounts.objects.filter(password=old_password)
        if user_auth.exists():

            u = Accounts.objects.get(username=email)
            print(u)
            # u.password =password
            # u.save()

            print('yes ho gya change')

            messages.success(request, 'Your Password Has been Changed !')
            return redirect('profile')
        else:
            messages.success(request, 'Please Enter old Password!')

    context = {
        'form': form,
    }
    return render(request,'change_password.html',context)

def account_logout(request):
    logout(request)
    return redirect('login')
