from django import forms
from django.contrib.auth.models import User
from .models import Game

user_db = User.objects

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['type'] = 'password'

'''class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('photo','user','mins_left')'''

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields =('name', 'desc', 'image')
        labels ={
            'desc': 'Description'
        }