from itertools import chain
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView,View, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# 로그인
@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('house_codition_show')
        
    if request.method == "POST":
        snackfor_id = request.POST['id']
        pw = request.POST['pw']

        user = auth.authenticate(request, username = snackfor_id, password=pw)
        if user is not None :
            if user.is_active is None :
                return render(request, 'account/login.html', { 'error' : '로그인 할 수 없습니다. 함부로 못들어오지!!' })
            else:    
                auth.login(request, user)
                return redirect('house_codition_show')
        else:
            return render(request, 'account/login.html', { 'error' : 'ID와 PW를 다시 확인하여주세요.' })
    else:
        return render(request, 'account/login.html')


# 로그아웃
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('login/');
