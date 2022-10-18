from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('login', views.loginfun, name='login'),
    path('signup',views.signupfun, name='signup')
]


urlpatterns += staticfiles_urlpatterns()