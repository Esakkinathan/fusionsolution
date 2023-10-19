
from django.urls import path
from .views import UserRegisterView,CustomLoginView,UserEditView,PasswordChangeView,password_success
from django.contrib.auth import views
from .forms import CustomLoginForm

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html')),
    path('password/',PasswordChangeView.as_view(),name='password_change'),
    path('password_success/',password_success,name='password_success'),
]