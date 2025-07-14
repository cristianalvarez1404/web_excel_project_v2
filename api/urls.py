from django.contrib import admin
from django.urls import path
from articles import urls

urlpatterns = [
    path('/', admin.site.urls),
]