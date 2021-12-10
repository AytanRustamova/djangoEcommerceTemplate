from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password #Djangonun validate_password funksiyasini oz formumuzda istifade edirik.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    
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
    






