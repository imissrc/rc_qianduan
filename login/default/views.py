from django.shortcuts import render,redirect,HttpResponse
from django.http import  HttpResponseRedirect
from default.forms import UserModelForm
from default.models import User,User_Info
from django.contrib import messages
from . import models
# Create your views here.

def islogining(request):
    print(request.session['user_id'])
    if request.session['user_id']=='':
        return False
    else:
        return True
def address_book(request):
    if not islogining(request):
        return HttpResponseRedirect('/')
    user_info=User_Info.objects.filter(user=request.session['user_id'])
    # print(user_info.user_id)
    return render(request,'address_book.html',{'user_info':user_info})
# def adduser(request):
#     if not islogining(request):
#         return HttpResponseRedirect('/')
#     if request.method == 'POST':
#         user_info=UserModelForm(request.POST)
#         if user_info.is_valid():
#             user_info.instance.user_id=request.session['user_id']
#             user_info.save()
#     else:
#         user_info=UserModelForm()
#     return render(request,'add_contantpeo.html',{'user_info':user_info})

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            peo = User.objects.get(username=username)
            if peo.password == password:
                request.session['user_id']=peo.id
                messages.success(request, '欢迎登陆')
                return redirect('/address_book/')
            else:
                messages.error(request, '密码不正确！')
        except:
            messages.error(request, '用户名不存在！')
    elif request.method == 'GET':
        return render(request,'login.html')

    return HttpResponseRedirect('/')  # 转回首页

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if not User.objects.filter(username=username).exists():
            peo=User(username=username,password=password)
            peo.save()
            messages.success(request,'注册成功')
            return HttpResponseRedirect('/')
        else:
            messages.error("该用户名已被注册")
            return render(request,'register.html')
    else:
        return render(request,'register.html')

# class UserForm(forms.Form):
#     username=forms.CharField(widget=forms.TextInput(attrs={'class':'text_field','id':'username'}))
#     password=forms.PasswordInput(widget=forms.PasswordInput(attrs={'class':'text_field','id':'password'}))
# class detail(request):
#     form=UserForm()
#     context={}
#     context['username']=form.username
#     context['password']=form.password
#def account(request):
 #   account_one=User(username="numberone",password="123456789")
  #
   #         username=res_form.cleaned_data['username']
    #        password=res_form.cleaned_data['password']
#
 #       return render(request, 'login.html',locals())
def logout(request):
    try:
        del request.session['user_id']
        return HttpResponseRedirect('/')
    except KeyError:
        pass
    messages.success(request,"已登出")

def add_contactpeo(request):
    if not islogining(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        return render(request, 'add_contantpeo.html')
    else:
        return HttpResponseRedirect('/address_book/')

def saveinfo(request):
    if not islogining(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        name=request.POST['name']
        qqnum = request.POST['qqnum']
        telnum = request.POST['telnum']
        mailnum = request.POST['mailnum']
        address = request.POST['address']

        user_info= User_Info()
        user_info.name=name
        user_info.qqnum = qqnum
        user_info.telnum = telnum
        user_info.mailnum = mailnum
        user_info.address = address

        user_info.user_id=request.session['user_id']
        user_info.save()
        return HttpResponseRedirect("/address_book/")
    else:
        name = request.GET['name']
        qqnum = request.GET['qqnum']
        telnum = request.GET['telnum']
        mailnum = request.GET['mailnum']
        address = request.GET['address']

        user_info = User_Info()
        user_info.name = name
        user_info.qqnum = qqnum
        user_info.telnum = telnum
        user_info.mailnum = mailnum
        user_info.address = address

    return render(request, 'add_contantpeo.html')

def updateinfo(request,infoid):
    if request.method=='GET':
        user_info=User_Info.objects.get(id=infoid)
        return render(request,'updateinfo.html',{'infoid':infoid,'user_info':user_info})
    elif request.method=="POST":
        name = request.POST['name']
        qqnum = request.POST['qqnum']
        telnum = request.POST['telnum']
        mailnum = request.POST['mailnum']
        address = request.POST['address']

        user_info = models.User_Info.objects.get(id=infoid)
        user_info.name = name
        user_info.qqnum = qqnum
        user_info.telnum = telnum
        user_info.mailnum = mailnum
        user_info.address = address
        user_info.save()
        return HttpResponseRedirect("/address_book/")
