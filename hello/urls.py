from django.conf.urls import url 
from hello import views

urlpatterns = [ 
    url('about', views.index),
]
