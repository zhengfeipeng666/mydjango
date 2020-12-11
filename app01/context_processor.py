# -*- coding: utf-8 -*-
# @Time : 2020/12/11 11:46
# @Author : wangchao
# @Email : wangchao8@tiens.com
# @File : context_processor.py
# @Project : MyDjanog

def first_page(request):
    Username = request.session["Username"]
    return {"Username": Username}