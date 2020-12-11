import base64

from django.db.models import Q,F
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib import auth

from apps.functional_test.models import *
import pager

# Create your views here.


# 用户登录
def login_action(request):
    if request.method=="GET":
        return render(request, "login.html")
    else:
        if request.method == "POST":
            Username = request.POST.get("username")
            Password = request.POST.get("password")
            user = auth.authenticate(username=Username, password=Password)
            if user != None:
                auth.login(request, user)
                request.session["Username"] = Username
                User.objects.filter(username=Username).update(pwd=base64.b64encode(bytes(Password, 'utf-8')).decode())
                # 批量添加数据
                # for i in range(3000):
                #      TestTable.objects.create(u_user='wangchao{}'.format(str(i)),
                #                                         addr='北京市海淀区苏州街',age=28)
                return redirect("/first_page/")
            else:
                return render(request, "login.html", {"error": "用户名或密码错误,请重新输入！"})


@login_required
def first_page(request):
    Username = request.session["Username"]
    return render(request, "first_page.html", {"Username": Username})


# 获取项目
@login_required
def get_projectitem(request):
    project_list = Project.objects.all()
    page_info = pager.PageInfo(request.GET.get('page'), len(project_list), 10, '/project.html', 20)
    obj_list = Project.objects.all()[page_info.start():page_info.end()]
    return render(request, 'project.html', {'obj_list': obj_list, 'page_info': page_info})

# 按照项目名称搜索
@login_required
def project_search(request):
    project_name = request.GET.get("project_name")
    select = request.GET.get("select")
    if select!='2':
        project_list = Project.objects.filter(Q(project_name__contains=project_name),Q(status=select)).order_by("-id")
        page_info = pager.PageInfo(request.GET.get('page'), len(project_list), 10, '/project.html', 20)
        obj_list = Project.objects.filter(Q(project_name__contains=project_name),Q(status=select)).order_by("-id")\
        [page_info.start():page_info.end()]
    else:
        project_list = Project.objects.filter(Q(project_name__contains=project_name)).order_by("-id")
        page_info = pager.PageInfo(request.GET.get('page'), len(project_list), 10, '/project.html', 20)
        obj_list = Project.objects.filter(Q(project_name__contains=project_name)).order_by("-id")\
        [page_info.start():page_info.end()]
    return render(request, 'project.html', {'obj_list': obj_list, 'page_info': page_info})


# 退出登录
def logout(request):
    auth.logout(request)
    return redirect(reverse('logout'))