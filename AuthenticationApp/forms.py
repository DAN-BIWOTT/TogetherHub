from django import forms
from .models import CustomUser  # Import your custom user model

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    security_question = forms.ChoiceField(
        label="Security Question",
        choices=[
            ("", "Select security question"),
            ("What is your favorite food?", "What is your favorite food?"),
            ("What is your favorite place?", "What is your favorite place?"),
            ("What is your favorite hero?", "What is your favorite hero?"),
            ("What is your favorite colour?", "What is your favorite colour?")
        ],
        required=True
    )
    # security_answer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your answer'}), max_length=255)

    security_answer = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your answer', 'autocomplete': 'off'}),
        max_length=255,
        required=True
    )
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        try:
            user = CustomUser.objects.get(email=email)
            cleaned_data['user'] = user  # Store user in cleaned_data
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("No user found with this email.")

        return cleaned_data
