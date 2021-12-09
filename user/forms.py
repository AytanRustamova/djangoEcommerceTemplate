from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password #Djangonun validate_password funksiyasini oz formumuzda istifade edirik.
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=127, validators=(validate_password,))
    password2 = forms.CharField(max_length=127, validators=(validate_password,))
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'gender', 
            'bio',
            'image'
        ]
        
    def clean(self): #Check password1 and password2 is same or not in HTML form without sending query.
        password1 = self.cleaned_data.get('password1'),
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('Passwords are not same!')
        return super().clean()
    






