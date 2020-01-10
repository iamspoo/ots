from . import views
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('signup/',views.signup,name='sign_up'),
    path('login/',views.login,name='log_in'),
    path('lostatus/',views.lostatus,name='lostatus'),
    path('sistatus/',views.sistatus,name='sistatus'),
    path('result/',views.result,name='result'),
    ]
