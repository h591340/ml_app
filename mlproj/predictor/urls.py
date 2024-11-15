from django.urls import path
from . import views

urlpatterns = [
    path('predict_salary/', views.predict_salary, name='predict_salary'),
    path('', views.predict_salary, name='index'),
    path('data/', views.data, name='data'),
]
