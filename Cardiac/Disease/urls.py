from django.urls import path
from .import views
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('result',views.result,name='result'),
    
    path("submit-heart-data", views.submit_heart_data, name="submit-heart-data"),
    
]