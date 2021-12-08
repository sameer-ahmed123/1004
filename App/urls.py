from django.urls import path
from . import views
urlpatterns =[
    path("emp",views.emp,name="emp")
]