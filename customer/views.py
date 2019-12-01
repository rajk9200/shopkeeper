from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomerForm
from .models import Customer
from register.models import Register
from django.contrib import messages

from accounts.models  import Accounts


from django.contrib.auth import logout
# Create your views here.

def customer_signup(request):

    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('signup')

        messages.add_message(request, messages.INFO, 'Customer Added Successfully !')
    d ={
        'form':form
    }


    return render(request,'customer/signup.html',d)

def show_customer(request):
    user_name = 'not_login'
    if not request.session.get('user_email', None):
        return redirect('login')
    else:
        email = request.session.get('user_email', None)
        user_name1 = Accounts.objects.filter(email=email)
        for i in user_name1:
            user_name = i.username

    if request.method=='POST':
        id_list = request.POST.getlist('instance')
        for cus_id in id_list:
            Customer.objects.get(id=cus_id).delete()


    c = Customer.objects.all()
    t = Register.objects.all()

    context ={
        'c':c,
        't':t,
    }

    return render(request,'customer/customers.html',context)

def update_customer(request,id):
    customer = Customer.objects.get(id=id)



    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('all_customers')

    d = {
        'form': form
    }
    return render(request,'customer/signup.html',d)


def delete_customer(request,id):
    customer =Customer.objects.get(id=id)
    if request.method =='POST':

        customer.delete()
        return redirect('all_customers')
    return render(request,'customer/confirm.html')
    # return HttpResponse("Data delete ho gya")


def customer_dashboard(request):

    mycus='not login'
    if not request.session.get('mycustomer', None):
        return redirect('login')
    else:
        mycus = request.session.get('mycustomer', None)



    c = Customer.objects.count()


    context = {
        'c': c,
        'mycus':mycus
    }

    return render(request,'dashbord.html',context)




