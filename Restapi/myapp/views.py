from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import Account
from .models import Detail
from django.shortcuts import get_object_or_404
def Home(request):
    return render(request, "Home.html")
def sign(request):
    if request.method=='POST':
        reg=Account(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        adress=request.POST['address']

        emailerror=""
        usererror=""
        if User.objects.filter(username=username).exists():
            usererror = "Username already exists"
        else:
            usererror = ""
        if User.objects.filter(email=email).exists():
            emailerror = "Email already exists"
            
        else:
            emailerror = ""
        context = {
            "form": reg,
            "emailerror": emailerror,
            "usererror": usererror,
            "formerror": ""
        }
        if emailerror != "" or usererror != "":
            return render(request, 'register.html', context)
        if reg.is_valid():
            user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            
            user.save()
            Detail(user=user,adress=adress).save()
            return redirect('/display/')
        else:
            reg=Account()
            return render(request,'register.html',{'fm':reg})
    else:
        reg=Account()
        return render(request,'register.html',{"fm": reg})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                form = AuthenticationForm()
                return  redirect("/user_detail/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"fm":form})
   

def logout_request(request):
     logout(request)
     return redirect("/")


def userdetail(request):
    if request.user.is_authenticated:
        user=User.objects.all();
        add=Detail.objects.all();
        return render(request,"table.html",{'users':user,'add':add})
    else:
        return redirect('/')


def user_delete(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            h=request.POST['pro_id']
            print(h) 
            user = User.objects.get(pk=id)
            user.delete()
            return redirect('/user_detail/')

