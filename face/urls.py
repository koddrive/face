
from django.contrib import admin
from django.urls import path,include
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('login.urls') ),
    path('', include ('main.urls') ),
    path('', include ('account.urls') ),
] 

