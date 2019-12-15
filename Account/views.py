from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import AccountForm
from .models import Account

# Create your views here.



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Account.statut = 1
            while Account.statut:
                return HttpResponse("""
            <h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
        """)

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = AccountForm()

    return render(request, 'html/name.html', {'form': form})
