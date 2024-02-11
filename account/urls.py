from django.contrib import admin
from django.urls import path, include
from account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/',views.account,name='account'),
    path('match/',views.match,name='match'),
    path('details/',views.details,name='details'),
    
]
