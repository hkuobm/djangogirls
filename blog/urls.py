from django.urls import path
from  . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),#viewを識別するために使われるURLの名前
]
