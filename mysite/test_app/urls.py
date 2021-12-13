
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login, register, home, user, company

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='test_app/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='test_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('user/', user, name='user'),
    path('company/', company, name='company')
]
