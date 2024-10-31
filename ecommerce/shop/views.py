from django.shortcuts import render,redirect
from shop.models import Category,Products
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def allcategories(request):
    k = Category.objects.all()
    return render(request, 'category.html', {'b': k})
def allproducts(request,p):
    c = Category.objects.get(name=p)
    p=Products.objects.filter(category=c)
    return render(request, 'product.html', {'c': c,'p':p})
def detail(request,p):
    p=Products.objects.get(name=p)
    return render(request,'detail.html',{'p':p})
def register(request):
    if (request.method == "POST"):
        n = request.POST['n']
        p = request.POST['p']
        c = request.POST['c']
        fname = request.POST['f']
        lname = request.POST['l']
        e=request.POST['e']
        ph=request.POST['ph']
        pl=request.POST['pl']
        if(p==c):
            u=User.objects.create_user(username=n,password=p,first_name=fname,last_name=lname,email=e,phone=ph,place=pl)
            u.save()
            return redirect('shop:home')
        else:
            return HttpResponse('password not matching')

    return render(request, template_name='register.html')

def user_login(request):
    if(request.method == "POST"):
        n=request.POST['n']
        p=request.POST['p']
        user=authenticate(username=n,password=p)
        if user:
            login(request,user)
            k = Category.objects.all()
            return render(request,'category.html',{'b':k})
        else:
            return HttpResponse("invalid")

    return render(request, template_name='login.html')
@login_required
def user_logout(request):
        logout(request)
        return redirect('shop:login')



