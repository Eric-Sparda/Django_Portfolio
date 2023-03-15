from django.urls import path
from . import views

urlpatterns = [
    path('',views.even, name = "Ever or Odd")

]