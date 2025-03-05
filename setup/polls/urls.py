from django.contrib import admin
from django.urls import path

from setup.polls import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/detail/', views.PollDetail.as_view(), name='poll_detail')
]
