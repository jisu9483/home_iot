from django.contrib import admin
from django.urls import path, include
from . import views     

urlpatterns = [    
    path('login/', views.login, name='login'),
    path('', include('django.contrib.auth.urls')),
]

"""
기본 장고 제공 페이지 수정시 참조
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
"""
