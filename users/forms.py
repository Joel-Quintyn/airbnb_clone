from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Check password"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=20, label="First Name")
    last_name = forms.CharField(max_length=20, label="Last Name")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            self.add_error(
                "email", forms.ValidationError("User already exists with that email")
            )
        except models.User.DoesNotExist:
            return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(
                "confirm_password", forms.ValidationError("Passwords do not match")
            )
        else:
            return password

    def save(self):

        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = models.User.objects.create_user(
            email, email, password, first_name=first_name, last_name=last_name
        )
