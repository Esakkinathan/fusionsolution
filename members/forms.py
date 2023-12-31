from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Enter Mail-id'}))
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Enter First Name'}))
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Enter Last Name'}),required=False)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        labels = {
            'username':'',
            'first_name':'',
            'last_name':'',
            'email':'',
            'password1':'',
            'password2':'',
        }
        
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark text-light'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control bg-dark text-light'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control bg-dark text-light'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter Password again'
        
        


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'hi',
        }
))
    
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control bg-dark text-light','placeholder':'example@mail.com'}))
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'elijah'}))
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Mikaelson'}),required=False)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    
    def __init__(self,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)        
        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark text-light'   
   

class PasswordChangingForm(PasswordChangeForm):
    old_password =  forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light','type':'password'}))
    new_password1 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light','type':'password'}))
    new_password2 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light','type':'password'}))
    
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
   