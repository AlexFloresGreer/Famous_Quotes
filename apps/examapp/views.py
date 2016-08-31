from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Quote, QuoteManager
from ..loginreg.models import User
from django.contrib import messages

# Create your views here.

def quotes(request):
    context={
        "quotes": Quote.objects.exclude(quote_joiner_id=request.session['user']),
        "favquotes": Quote.objects.filter(quote_joiner_id=request.session['user']),
        "name": request.session['name']
    }
    return render(request, 'loginreg/quotes.html', context)

def addquote(request):
    created_quote = Quote.quoteManager.create_quote(request.POST)
    if created_quote[0] == False:
        for error in created_quote[1]:
            messages.add_message(request,messages.INFO,error)
        return redirect('/quotes')
    if created_quote[0] == True:
        quote = Quote.objects.create(quoted_by=request.POST['quoted_by'], message=request.POST['message'], quote_creator_id=User.objects.get(id=request.session['user']))

    print "create " *10
    return redirect('/quotes')

def addtofav(request, id):
    quote = Quote.objects.get(id=id)
    quote.quote_joiner_id.add(User.objects.get(id=request.session['user']))
    quote.save()
    return redirect('/quotes')

def removefromfav(request, id):
    quote = Quote.objects.get(id=id)
    quote.quote_joiner_id.remove(User.objects.get(id=request.session['user']))
    quote.save()
    return redirect('/quotes')

def quotecount(request, id):
    user_row = User.objects.get(id=id)
    context = {
        "name": user_row.first_name,
        "quotes":  Quote.objects.filter(quote_creator_id=id)
    }
    return render(request, 'examapp/quotecount.html', context)
