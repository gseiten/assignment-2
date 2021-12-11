
from django.urls import path
from .views import index, home, user, company

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('user/', user, name='user'),
    path('company/', company, name='company')
]
