from . import views
from django.urls import path, include

urlpatterns = [
    path('show/', views.House_Codition_Show.as_view(), name='house_codition_show' ),
]
