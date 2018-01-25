from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder':'Your name...'}
        )
    )

    email = forms.CharField(
        label="Email",
        max_length=100,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder':'Your email address...'}
        )
    )

    message = forms.CharField(
        label="Message",
        max_length=100,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder':'Your message...'}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        max_length = 100,
        widget = forms.TextInput(
            attrs = { 'class': 'form-control' }
        )
    )

    password = forms.CharField(
        label = "Password",
        max_length = 20,
        widget = forms.PasswordInput(
            attrs = { 'class': 'form-control' }
        )
    )
