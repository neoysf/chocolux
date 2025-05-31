from django import forms
from .models import ContactMessage
from .models import UserEmail

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'phone_number', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email.'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number.'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message', 'rows': 4}),
        }

class EmailForm(forms.ModelForm):
    class Meta:
        model = UserEmail
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email.'}),
        }