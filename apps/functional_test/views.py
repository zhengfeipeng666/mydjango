from app01.views import login_action
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.db.models import Q,F
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from apps.functional_test.models import *
import pager
import base64

# Create your views here.


#根据登录用户获取模块数据
def get_filiterdata(request):
    # 获取当前登录用户登录名
    current_user_set = str(request.user.username)
    user_queryset=User.objects.filter(username=current_user_set)
    for user in user_queryset:
        return user.modules_set.all()

# 得到项目名名称
#把测试项目的project_name取出，当成新增编辑页面项目的可选的列
def get_project_name(filiterdata):
    project_set = set()
    for filiter in filiterdata:
        if filiter.Project.status:
            project_set.add(filiter.Project)
    project_obj_list=list(project_set)
    return project_obj_list



def modules_tester(request,modules_list):
    """
    :param modules_lsit: 模块列表
    :param project_list:项目列表
    modules_tester_list：
    :return: page_info:分页对象
              obj_lsit: 点击页码后分页每页返回的数据条数
    """
    modules_tester_list = []
    for obj in modules_list:
        tester_name = []
        # obj.Testers.all()返回的是auth.user表的对象，tester是其中的一行数据，tester.username是对应的测试人员姓名
        for tester in obj.Testers.all():
            tester_name.append(tester.username)
        modules_tester_list.append((obj, ' '.join(tester_name)))
    page_info = pager.PageInfo(request.GET.get('page'), len(modules_list), 10, '/functional_test/get_modules', 20)
    obj_list = modules_tester_list[page_info.start():page_info.end()]
    return page_info,obj_list


@login_required
def get_modules(request):
    # 获得登录用户名下的模块
    modules_list = get_filiterdata(request)
    # 过滤禁用状态的项目名称
    project_list = get_project_name(modules_list)
    if request.method == 'GET':
        page_info,obj_list=modules_tester(request,modules_list)
        return render(request, 'functional_test/get_modules.html', {'obj_list':obj_list,'project_list':project_list,
                                                                        'page_info': page_info})
    elif request.method=='POST':
        print(request.method)
        # 获取输入条件
        modules_name = request.POST.get('modules_name')
        project_name = request.POST.get('project_name')
        status = request.POST.get('select')
        if len(modules_name)>0 and project_name=='0' and status=='2':
            # 以模块名称为查询条件
            modules_list = Modules.objects.filter(Modules_name=modules_name)
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html', {'obj_list': obj_list, 'project_list': project_list,
                                                                        'page_info': page_info})

        elif len(modules_name)>0 and project_name!='0' and status=='2':
            pro = Project.objects.get(id=int(project_name))
            modules_list = Modules.objects.filter(Project=pro,Modules_name=modules_name)
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html',
                          {'obj_list': obj_list, 'project_list': project_list,'page_info': page_info})

        elif len(modules_name)>0 and project_name!='0' and status!='2':
            pro = Project.objects.get(id=int(project_name))
            modules_list = Modules.objects.filter(Project=pro,Modules_name=modules_name,status=status)
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html',
                          {'obj_list': obj_list, 'project_list': project_list,'page_info': page_info})

        elif project_name!='0' and status!='2':
            pro = Project.objects.get(id=int(project_name))
            modules_list = Modules.objects.filter(Project=pro,status=status)
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html',
                          {'obj_list': obj_list, 'project_list': project_list,'page_info': page_info})

        elif project_name!='0' and status=='2':
            pro = Project.objects.get(id=int(project_name))
            modules_list = Modules.objects.filter(Project=pro)
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html',
                          {'obj_list': obj_list, 'project_list': project_list, 'page_info': page_info})

        elif status!='2':
            modules_list = Modules.objects.filter(status=status)
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html',
                          {'obj_list': obj_list, 'project_list': project_list,'page_info': page_info})

        # 如果没有输入任何搜索条件，返回全体数据
        if len(modules_name)==0 and status=='2' and project_name=='0':
            page_info, obj_list = modules_tester(request, modules_list)
            return render(request, 'functional_test/get_modules.html',
                          {'obj_list': obj_list, 'project_list': project_list,'page_info': page_info})

























# @login_required
# def search(request):
#     """处理搜索"""
#     value = request.POST.get("search")
#     # 如果用户输入搜索值，按搜索值检索数据并返回
#     if value:
#         all_count = TestTable.objects.filter(u_user=value)
#         if len(all_count) < 1:
#             return render(request, 'first_page.html')
#         else:
#             page_info = pager.PageInfo(request.GET.get('page'), len(all_count), 10, '/first_page', 20)
#             obj_list = TestTable.objects.filter(u_user=value)[page_info.start():page_info.end()]
#             return render(request, 'first_page.html', {'obj_list': obj_list, 'page_info': page_info})
#     else:
#         user_list = TestTable.objects.all()
#         page_info = pager.PageInfo(request.GET.get('page'), len(user_list), 10, '/first_page', 20)
#         obj_list = TestTable.objects.all()[page_info.start():page_info.end()]
#         return render(request, 'first_page.html', {'obj_list': obj_list, 'page_info': page_info})






