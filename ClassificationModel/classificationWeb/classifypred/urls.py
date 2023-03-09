from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('TEST/',views.testHealth,name="healthCheck"),
    path('testpage/',views.testPage,name="TestPage"),
    path('LoginPage/',TemplateView.as_view(template_name='login.html')),
    path('login/',views.login,name='login')
]
