from django.urls import path,include
from . import views

urlpatterns = [
    
    path('login', views.loginfun, name='login'),
    path('signup',views.signupfun, name='signup')
]


