from django.urls import path, include
from . import views
from django.conf.urls import handler404

from .views import pageNotFound, serverError

urlpatterns = [
   path('', views.index, name='home'),
   path('info/',views.info, name='info'),
   path('new/', views.new_home, name='new_home'),
   path('feedback/', views.feedback_home, name='feedback_home'),
   path('feedback/create',views.create, name='create'),
   path('buy/', views.buy, name='buy'),
   path('buy/vce/', views.vce, name='vce'),
   path('history/', views.history, name='history'),
   path('', include('django.contrib.auth.urls')),
   path('register/', views.Register.as_view(), name='register'),
   path('accounts/logout/', views.user_logout, name='logout_user'),
]


