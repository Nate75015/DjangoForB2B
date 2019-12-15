from django import forms

class AccountForm(forms.Form):
    mail = forms.EmailField(label="Votre adresse e-mail")
    password = forms.CharField(max_length=255, help_text=u"Please enter your name...")
