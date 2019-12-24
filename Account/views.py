from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import AccountForm, ResetForm
from .models import Account
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime





def Login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            MAIL = form.cleaned_data.get('mail')
            PASSWORD = form.cleaned_data.get('password')
            DIC = {'mail' : MAIL, 'password' : PASSWORD}
            if DIC in Account.objects.values('mail', 'password'):
                Account.statut = True
                while Account.statut:
                    return redirect('/home/')
            else:
                    return redirect('/login/')
        else:
            return redirect('/login/')
    else:
        if Account.statut == True:
            return redirect('/home/')
        else:
            form = AccountForm()
            return render(request, 'login.html', {'form': form})



def Home(request):
    if Account.statut == True:
        return render(request, 'home.html', {'date': datetime.now()})
        #return render(request, 'home2.html')
    else :
        return redirect('/login/')
    #return HttpResponse("""
    #    <h1>Bienvenue sur mon blog !</h1>
    #    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    #""")


def Logout(request):
    Account.statut = False
    return HttpResponseRedirect('/login/')


def ChangePassword(request):
    if Account.statut == True :
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ResetForm(request.POST)
            if form.is_valid():
                if form.cleaned_data.get('NewPassword') == form.cleaned_data.get('ConfirmedPassword'):
                    Account.objects.filter(mail = form.cleaned_data.get('mail')).values_list('password', flat=True).update(password = form.cleaned_data.get('NewPassword'))
                    return redirect('/home/')
                else :
                    return redirect('/ChangePassword/')
        else :
            form = ResetForm()
            return render(request, 'ResetPassword.html', {'form': form})
    else :
        return redirect('/login/')
