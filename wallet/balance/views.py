from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Signup, Transaction
from django.contrib.auth import authenticate, logout,login
from datetime import date

# Create your views here.
#
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id= request.user.id)
    data = Signup.objects.get(user= user)
    transaction = Transaction.objects.filter(user= user)

    error=""
    if request.method == "POST":
        u = User.objects.filter(username=request.user.username).first()

        try:
            if request.POST.get('credit') == "1":
                data.balance += int(request.POST['amount'])
                data.save()
                Transaction.objects.create(user=u , amount=request.POST['amount'], cr_dr="credit")
                error = "no"
            else:
                data.balance -= int(request.POST['amount'])
                data.save()
                Transaction.objects.create(user=u , amount=request.POST['amount'], cr_dr="debit")
                error = "no"

        except:

            error = "yes"
    return render(request,'home.html',context={'transaction':transaction,'data':data, 'error':error})


def delete_history(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id= request.user.id)
    data = Signup.objects.get(user= user)
    transaction = Transaction.objects.get(id=pid)

    cr_dr_type = transaction.cr_dr
    amount = transaction.amount

    if cr_dr_type == "credit":
        data.balance -= amount
        data.save()
        transaction.delete()
    else:
        data.balance += amount
        data.save()
        transaction.delete()



    return redirect('home')

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user= authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def signup1(request):
    error=""
    if request.method == "POST":
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['emailid']
        p = request.POST['password']
        b = request.POST['balance']
        try:
            user = User.objects.create_user(username=e, password=p , first_name=f , last_name=l)
            Signup.objects.create(user=user, balance=b)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'signup.html',d)

def Logout(request):
    logout(request)
    return redirect('login.html')
