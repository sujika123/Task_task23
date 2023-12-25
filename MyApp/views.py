from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from MyApp.forms import LoginForm, userloginform, taskform
from MyApp.models import task


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = LoginForm()
    form1 = userloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            usr = form1.save(commit=False)
            usr.user = user
            usr.save()
            return redirect("loginview")
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')


def userhome(request):
    return render(request,'userhome.html')


def addtask(request):
    form = taskform()
    u = request.user
    if request.method == 'POST':
        form = taskform(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('viewtask')
    return render(request,'addtask.html',{'form':form})


def viewtask(request):
    u = request.user
    data=task.objects.filter(user=u)
    return render(request,'viewtask.html',{'data':data})

# def tviewnotes(request):
#     u = request.user
#     data = addnotes.objects.filter(user=u)
#     return render(request,'teacher/tviewnotes.html',{'data':data})


def taskupdate(request, id):
    user = task.objects.get(id=id)
    form = taskform(instance=user)
    if request.method == "POST":
        form = taskform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewtask')
    return render(request, 'updatetask.html', {'form': form})


def taskdelete(request, id):
    data=task.objects.get(id=id)
    data.delete()
    return redirect('viewtask')
