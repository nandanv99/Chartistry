from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.main),
    path('upload_csv',views.upload_csv),
]