from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.main),
    path('upload_csv',views.upload_csv),
    path("block_analysis",views.block_scan),
    path("block_analysis_page",views.block_scan_analysis),
    path('process_form', views.process_form, name='process_form'),
    path('type_csv', views.csv_page),
]