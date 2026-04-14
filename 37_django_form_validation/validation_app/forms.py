from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'age', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
        }

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name')
        # Check if all characters are either letters or spaces without using 're'
        if not all(char.isalpha() or char.isspace() for char in name):
            raise forms.ValidationError("Full name should only contain letters and spaces.")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to register.")
        if age > 100:
            raise forms.ValidationError("Please enter a realistic age.")
        return age
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
             raise forms.ValidationError("Only .com email addresses are allowed for this lab.")
        return email
