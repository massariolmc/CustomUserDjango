from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('index/',views.index, name='index'),
    path('signup/', views.signup, name = 'signup')
]