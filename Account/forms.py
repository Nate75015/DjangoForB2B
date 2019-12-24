from django import forms

class AccountForm(forms.Form):
    mail = forms.EmailField(label="Votre adresse e-mail")
    password = forms.CharField(max_length=255, help_text=u"Votre mot de passe")

class ResetForm(forms.Form):
    mail = forms.EmailField(label="Votre adresse e-mail")
    NewPassword = forms.CharField(max_length=255, help_text=u"Nouveau mot de passe ")
    ConfirmedPassword =  forms.CharField(max_length=255, help_text=u"Confirmer le mot de passe")
