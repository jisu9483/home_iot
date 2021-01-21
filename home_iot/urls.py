from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', RedirectView.as_view(url='login') ),
    path('', include('account.urls')),
    path('admin/', admin.site.urls),
    path('house_condition/', include('house_condition.urls')),
]
