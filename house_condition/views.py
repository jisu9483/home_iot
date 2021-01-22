import json
import csv
import io
import requests
import os
import re
import serial

from collections import defaultdict
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Case, When, Subquery, OuterRef,IntegerField, F, Func, Value, CharField
from django.db.models.functions import Cast,ExtractHour, ExtractMinute
from django.db import models

from .models import ConditionRecord

# 집 컨디션 조회
class House_Codition_Show(View):
    templates_name = "house_condition/house_condition_show.html"
    
    def get(self, request):
        # 날씨 API 통신 웹사이트 openweathermap
        with open('secrets.json') as js :
            data = json.load(js)

        WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q=seoul&appid='+data['WEATHER_API_KEY']  
        response = requests.get(WEATHER_URL).json()
        
        current_temperature = response['main']['temp'] - 273.15
        current_humidity = response['main']['humidity']
        weather_status = response['weather'][0]['main']

        record = ConditionRecord.objects.all()\
                    .values('record_time','temperature','humidity')\
                    .annotate(
                            hour=ExtractHour('record_time'),
                            minute=ExtractMinute('record_time'),
                            )\
                    .order_by('-id')[0:6]
        context = {
            'record':reversed(record),
            'data':json.dumps(list(reversed(record)), cls=serializers.json.DjangoJSONEncoder),
            'current_temperature':round(current_temperature,1),
            'current_humidity':current_humidity,
            'weather_status':weather_status,
        }
        return render(request, self.templates_name, context)

# 온습도 값 받아오기 10분에 한번
class Request_Data_Save(View):    
    def get(self, request):
        temperature = self.request.GET.get('temperature','0.0')
        humidity = self.request.GET.get('humidity','0.0')
        # # 집온도가 34도 일시 알람
        # if float(temperature) > 34:
        #     on_air_conditioner = True
        # else:
        #     on_air_conditioner = False

        # 받아온 값 저장
        record_save = ConditionRecord.objects.create(
                    temperature = float(temperature),
                    humidity = float(humidity), 
                )
        return HttpResponse(status=200)

# 수동 에어컨 On/Off
class Air_Condition_Manual(View):    
    def get(self,request):
        status_code = self.request.GET.get('status','')
        arduino = serial.Serial('COM3', 9600, timeout=5)
        # 에어컨 on/off test
        if status_code == "On":
            d = 'Y';
            arduino.write(d.encode('utf-8'))
        else:
            d = 'N';
            arduino.write(d.encode('utf-8'))
        data = {}
        return JsonResponse(data)
