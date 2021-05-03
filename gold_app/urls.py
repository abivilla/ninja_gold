from django.urls import path
from . import views

urlpatterns = [
    path('', views.display),
    path('process_money', views.process),
    path('reset', views.reset),
]
