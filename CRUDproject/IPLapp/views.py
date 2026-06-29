from collections import UserDict, UserList
from multiprocessing import context

from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from IPLapp.models import players 
from django.shortcuts import render,redirect

from IPLapp.models import players

# Create your views here.
def index_view(request):
    return render(request,'home.html')

def create_view(request):
    if(request.method=='POST'):
        print(request.POST)

        j=request.POST.get('jn')
        n=request.POST.get('pn')
        r=request.POST.get('rn')
        w=request.POST.get('wk')

        obj=players(jn=j, pname=n,run=r,wickets=w)
        obj.save()

        return redirect('/iplapp/display/')
    


    return render(request,'create.html')


def display_view(request):

    db=players.objects.all()
    context={"db":db}
    return render(request,'display.html',context)


def delete_view(request,n):
    obj=players.objects.get(pname = n)
    obj.delete()
    return redirect('/iplapp/display/')

    



def update_view(request,n):
     obj=players.objects.get(pname = n)
     {"p":obj}

     if(request.method =="POST"):
         
        u_j=request.POST.get('jn')
        u_n=request.POST.get('pn')
        u_r=request.POST.get('rn')
        u_w=request.POST.get('wk')

        obj.jn=u_j
        obj.pname=u_n
        obj.run=u_r
        obj.wickets=u_w
        obj.save()
        return redirect('/iplapp/display/')
         
     return render(request,'update.html', {"p":obj})


def register_view(request):
    if (request.method=="POST"):
     print(request.POST)
     uname=request.POST.get("uname")
     em=request.POST.get("em")
     pwd=request.POST.get("pwd")

     if(User.objects.filter(username=uname).exists()):
         return render(request,'register.html',{'err':'User already exist'})
 
     User.objects.create_user(username=uname,email=em,password=pwd)
     return redirect("/iplapp/login/")
    
    return render(request,'register.html')
    


def login_view(request):

    if (request.method=="POST"):
     print(request.POST)
     uname=request.POST.get("uname")
     pwd=request.POST.get("pwd")

     user=authenticate(request,username=uname,password=pwd)

     if user is None:
         return render(request,'login.html',{'err':'Invalid User name and password'})
     else:
         login(request,user)
         return redirect('/iplapp/create/')

    return render(request,"login.html")