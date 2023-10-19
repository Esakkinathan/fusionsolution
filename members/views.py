from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm,CustomLoginForm,EditProfileForm,PasswordChangingForm
from django.contrib.auth.views import LoginView,PasswordChangeView
# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html' 
    authentication_form = CustomLoginForm  
    redirect_authenticated_user = True

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    #success_url = reverse_lazy('home')
    
def password_success(request):
    return render(request,'registration/password_success.html',{})