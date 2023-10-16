
from django.urls import path
from .views import UserRegisterView,CustomLoginView
from django.contrib.auth import views
from .forms import CustomLoginForm
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path(
        'login/',
        views.LoginView.as_view(
            template_name="login.html",
            authentication_form=CustomLoginForm
            ),
        name='login')
]
