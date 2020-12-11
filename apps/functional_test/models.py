
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    project_name=models.CharField(max_length=20,verbose_name="项目名")
    project_desc = models.CharField(max_length=200, blank=True, verbose_name="项目描述")
    status= models.BooleanField( verbose_name="状态")

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.project_name


#模块表
class Modules(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name="项目名")
    Modules_name=models.CharField(max_length=20,verbose_name="模块名")
    Testers=models.ManyToManyField('auth.User',blank=True,verbose_name="测试人员")
    Developer = models.CharField(max_length=100,blank=True,verbose_name="开发人员")
    Modules_desc = models.CharField(max_length=200, blank=True, verbose_name="模块描述")
    status = models.BooleanField(verbose_name="状态")

    class Meta:
        verbose_name = '模块'
        verbose_name_plural = '模块'

    def __str__(self):
        return self.Modules_name

# 用户表
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField()


class TestTable(models.Model):
    u_user = models.CharField(max_length=30)
    addr = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        verbose_name = '测试使用'
        verbose_name_plural = '测试使用'


# 添加用户表的另一个密码字段
# 先定义一个字段
pwd_field = models.CharField(max_length=30, default="")
# 将字段添加到表中
pwd_field.contribute_to_class(User, 'pwd')