import json
import csv
import io

from collections import defaultdict
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Case, When, Subquery, OuterRef,IntegerField
from django.db import models

from .models import ConditionRecord

# 집 컨디션 조회
class House_Codition_Show(View):
    templates_name = "house_condition/house_condition_show.html"

    def get(self, request):
        record = ConditionRecord.objects.all()[0:12]
        context = {}
        return render(request, self.templates_name, context)