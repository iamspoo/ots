from django.shortcuts import render
from django.http import HttpResponse
from .models import customer
from .models import order


def login(request):
    return render(request,'otsapp/login.html')

def signup(request):
    return render(request,'otsapp/signup.html')

def lostatus(request):
    uname=request.POST.get("name1")
    pword=request.POST.get("password")
    cus=customer.objects.all()
    dic={"city":"default",}
    for c in cus:
        if(c.name==uname and c.password==pword):
            dic["city"]=c.city
            break
    if(dic["city"]=="default"):
        dic["city"]="passwort incorect"
    if(dic["city"]=="passwort incorect"):
        return render(request,'otsapp/login.html')
    else:
        return render(request,'otsapp/status.html',dic)

def sistatus(request):
    uname=request.POST.get("name1")
    pnum=request.POST.get("phonenum")
    addr=request.POST.get("address")
    city=request.POST.get("city")
    state=request.POST.get("state")
    pword=request.POST.get("password")
    cusobj=customer(name=uname,phone=pnum,address=addr,city=city,state=state,password=pword)
    cusobj.save()
    return render(request,'otsapp/status.html')

def result(request):
    od=request.POST.get("order id")
    orde=order.objects.all()
    dic={}
    for o in orde:
        if(o.orderid==od):
            dic["status"]=o.status
            dic["name"]=o.name
            break
    cus=customer.objects.all()
    for c in cus:
        if(dic["name"]==c.name):
            dic["phone"]=c.phone
            dic["address"]=c.address
            dic["ciyt"]=c.city
            dic["state"]=c.state
    return render(request,'otsapp/result.html',dic)
