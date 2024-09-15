from django.shortcuts import render,redirect
from home.models import Employees
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.
@never_cache
def loginPage(request):
    if "username" in request.session:
        return redirect(homePage)
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        employee=None
        employee = Employees.objects.filter(username=username)
        if employee.exists():
            employee=employee.first()
            if employee.password==password:
                request.session['username']=username
                return redirect(homePage)
            else:
                messages.error(request,"Username or password does not exist")
                return redirect(loginPage)
        else:
                messages.error(request,"Username or password does not exist")
                return redirect(loginPage)
            
    return render(request,'login.html')  

def signupPage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        emp=Employees(
            name=name,
            username=username,
            email=email,
            password=password
        )
        emp.save()
        return redirect(loginPage)
    return render(request,'signup.html')

def homePage(request):
    if "username" in request.session:
        username=request.session['username']
        emp=Employees.objects.get(username=username)
        context={
            'emp':emp
        }
        return render(request,'home.html',context)
    return redirect(loginPage)

@never_cache
def adminLoginPage(request):
    if "username" in request.session:
        return redirect(adminPanel)
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            if request.user.is_staff:
                request.session['username']=username
                return redirect(adminPanel)
            else:
                messages.error(request,"Super user is not exist!!,check username or password")
                return redirect(adminLoginPage)
        else:
            messages.error(request,"Super user is not exist!!,check username or password")
            return redirect(adminLoginPage)
    return render(request,'adminLogin.html')


def adminPanel(request):
    if "username" in request.session:
        emp =Employees.objects.all()

        context={
            'emp':emp
        }
        return render(request,'adminPanel.html',context)
    return redirect(adminLoginPage)



def addPage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        emp=Employees(
            name=name,
            username=username,
            email=email,
            password=password
        )
        emp.save()
        return redirect('adminpanel')
    return render(request,'adminPanel.html')

def editPage(request):
    emp=Employees.objects.all()
    
    context={
        'emp':emp
    }
    return redirect(request,'adminPanel.html',context)

def updatePage(request,id):
    if request.method=='POST':
        name=request.POST.get("name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        emp=Employees(
            id=id,
            name=name,
            username=username,
            email=email,
            password=password
        )
        emp.save()
        return redirect('adminpanel')
    return render(request,'adminPanel.html')

def deletePage(request,id):
    emp=Employees.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp
    }
    return redirect('adminpanel')
def searchPage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        emp=Employees.objects.filter(username=username)
        context={
            'emp':emp
        }
    return render(request,'search.html',context)

def logout_view(request):
    if 'username' in request.session:
        request.session.flush()
        return redirect(loginPage) 
