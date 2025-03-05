from django.urls import path

from setup.accounts import views


urlpatterns = [
    path('login/', views.Login.as_view(), name='login')
]