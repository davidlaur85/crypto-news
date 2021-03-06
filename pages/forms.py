from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(
        label = "Name",
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Your name...'
            }
        )
    )

    email = forms.CharField(
        label = "Email",
        max_length=100,
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Your email address...'
            }
        )
    )

    message = forms.CharField(
        label = "Message",
        max_length = 100,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder':'Your message...'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        max_length = 40,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        label = "Password",
        max_length = 50,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user_qs = User.objects.filter(username=username)
            if user_qs.count() == 0:
                raise forms.ValidationError("The user does not exist")
            else:
                user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label = "Username",
        max_length = 40,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Your username..."
            }
        )
    )

    email = forms.CharField(
        label = "Email",
        max_length = 80,
        widget = forms.EmailInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Your email address..."
            }
        )
    )

    password = forms.CharField(
        label = "Password",
        max_length = 50,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )

    re_password = forms.CharField(
        label = "Retype Password",
        max_length = 50,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "re_password"
        ]

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("Passwords must match")
        return password


class SubmitForm(forms.Form):
    title = forms.CharField(
        label = "Title",
        max_length = 300,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex: Buildings Will be Sold with Bitcoin"
            }
        )
    )

    url = forms.CharField(
        label = "Source",
        widget = forms.URLInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex: https://ccn.com/buildings-will-be"
            }
        )
    )
