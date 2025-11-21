from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date
            
class FeedbackForm(forms.ModelForm):
    class Meta:
        rates = {rate: rate for rate in range(1, 6)}
        model = Feedback
        fields = ['username', 'text', 'rate']
        
        widgets = {
            'text' : forms.Textarea,
            'rate': forms.Select(choices=rates),
            'username': forms.TextInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control-plaintext'
            }),
        }
        
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'article', 'price', 'in_stock', 'providers', 'category']
        
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 15}),
        }
        
class AddProviderForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+37529\d{7}$',
                message="Phone number must be in the format: '+37529XXXXXXX'"
            )
        ]
    )

    class Meta:
        model = Provider
        fields = ['name', 'address', 'phone_number']

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(
        required=True,
        label="Phone Number",
        max_length=13,
        #validators=[
        #    RegexValidator(
        #        regex=r'^\+37529\d{7}$',
        #        message="Phone number must be in the format: '+37529XXXXXXX'"
        #    )
        #]
    )
    age = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'max': date.today().isoformat()} ),
        label="Date of Birth"
    )
    #age = forms.IntegerField(required=True, 
    #                         min_value=18,
    #                         max_value=120,
    #                         error_messages={
    #                         'min_value': 'You must be at least 18 years old.',
    #                         'max_value': 'Please enter a valid age under 120.'},
    #                         label="Age")
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        
    def save(self, commit=True):
        user = super().save(commit)
        age = self.cleaned_data.get('age')

        Profile.objects.create(user=user, age=age)
        return user
    
