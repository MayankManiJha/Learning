from django.urls import path
from . import views

urlpatterns=[
    path('TEST/',views.testHealth,name="healthCheck"),
]
