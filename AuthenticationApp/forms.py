from django import forms
from .models import CustomUser  # Import your custom user model

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        try:
            user = CustomUser.objects.get(email=email)
            cleaned_data['user'] = user  # Store user in cleaned_data
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("No user found with this email.")

        return cleaned_data
