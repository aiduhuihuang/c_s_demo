from  django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from appone.models import *

#设置cookie
def set_cookie(request):
    response=HttpResponse(" ")
    response.set_cookie("username","zhangsan")
    print("_____________________________")
    response.set_cookie("age",100)
    return response
    # return HttpResponse("下发cookie")
#获取cookie
def get_cookie(request):
    username=request.COOKIES.get("username")
    print(username)
    return HttpResponse("获取cookie")
#删除cookie
def del_cookie(request):
    response=HttpResponse("删除cookie")
    #要删除什么就传什么参数
    response.delete_cookie("age")
    return response


#设置session
def set_session(request):
    request.session["username"]="lisi"
    return HttpResponse(request)
#获取session
def get_session(request):
    username=request.session.get("username")
    return HttpResponse(username)
#删除session
def del_session(request):
    # username=request.session.get("username")
    # print(username)
    del request.session["username"]
    return HttpResponse("删除session")


#密码加密
import  hashlib
def setpassword(pwd):
    md5=hashlib.md5()
    md5.update(pwd.encode())
    result=md5.hexdigest()
    return result
#登录功能的实现
def login(request):
    #判断登录
    #获取值
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(setpassword(password))
        if username and password:
            uses_obj=Users.objects.filter(username=username,password=setpassword(password)).first()
            if uses_obj:
                response=HttpResponseRedirect("/")#这个代表ip和端口进入的那个页面
                #下发cookie和session
                response.set_cookie("username",uses_obj.username)
                request.session["username"]=uses_obj.username
                return response

            else:
                return HttpResponseRedirect("/login/")
        else:
           return  HttpResponseRedirect("/login/")
    return render(request,"login.html",locals())

#loginout清除session和cookie
def loginout(request):
    response=HttpResponseRedirect("/")
    response.delete_cookie("username")
    del request.session["username"]
    return response
#第一种：公共函数实现
def yanzheng(re):
    cook_name = re.COOKIES.get("username")
    print(cook_name)
    sess_name = re.session.get("username")
    print(sess_name)
    if cook_name and sess_name and cook_name == sess_name:
        return True
    else:
        return False

#第二种：装饰器格式
def xiaoyan(fun):
    def inner(*args,**kwargs):
        return  fun(*args,**kwargs)
    return inner
#首页--登录了的才能访问这个页面
def index(request):

    if yanzheng(request):
        return  render(request,"index.html",locals())
    else:
        return  HttpResponseRedirect("/login/")

#about页面也要实现校验,登录了才能访问
def about(request):
    if yanzheng(request):
        return render(request,"about.html",locals())
    else:
        return HttpResponseRedirect("/login/")