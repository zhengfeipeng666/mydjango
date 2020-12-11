from django.contrib import admin
from apps.functional_test import models


# Register your models here.
class Project_search(admin.ModelAdmin):
    list_display = ["id","project_name","project_desc","status"]
    search_fields = ["project_name","status"]
    # 过滤器
    list_filter = ["project_name","status"]
    list_per_page = 10
    # ordering设置默认排序，负号表示降序
    # ordering = ('-id',)


class Models_search(admin.ModelAdmin):
    # 列表中显示的字段
    list_display = ["id","Modules_name","Developer","Modules_desc","status","Project"]
    # 可搜索的字段
    search_fields = ["Modules_name","status"]
    # 过滤器
    list_filter = ["Modules_name","status"]
    list_per_page = 10


admin.site.site_title = "今日买买"
admin.site.site_header = "接口测试后台管理"
admin.site.register(models.Project,Project_search)
admin.site.register(models.Modules,Models_search)