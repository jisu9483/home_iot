from . import views
from django.urls import path, include

urlpatterns = [
    path('show/', views.House_Codition_Show.as_view(), name='house_codition_show'),
    path('data_save/', views.Request_Data_Save.as_view(), name='request_data_save'),
    path('air_condition_manual/', views.Air_Condition_Manual.as_view(), name='air_condition_manual')
]
