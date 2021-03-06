from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import Quote, Like
from django.contrib.auth.models import User
from datetime import datetime
import json

def username_to_user(username):
    return User.objects.get(username=username)

def index(request):

    quotes = Quote.objects.all()

    if request.user.is_authenticated():
        liked_quote_ids = [x.quote_id for x in Like.objects.filter(user=request.user)]
    else:
        liked_quote_ids = []

    data = {'quotes': quotes, 'liked_quote_ids': liked_quote_ids}
    return render(request, 'quotes/index.html', data)

def dashboard(request, username):

    #user = User.objects.get(username=username)
    user = username_to_user(username)
    my_quotes = Quote.objects.all().filter(author=user.username)
    liked_quotes = Like.objects.all().filter(user=user)

    liked_quote_ids = [x.quote_id for x in liked_quotes]
    liked_quotes = [x for x in Quote.objects.all() if x.id in liked_quote_ids]

    data = {'liked_quotes': liked_quotes, 'liked_quote_ids': liked_quote_ids,
            'my_quotes': my_quotes}

    return render(request, 'quotes/dashboard.html', data)

def dashboard_details(request, username):

    # Mock data, get description from user in DB
    data = {'description': 'This is a sample description from the view'}
    return JsonResponse(data)

def already_liked_quote(user, quote_id):
    return Like.objects.filter(user=user, quote_id=quote_id).exists()

def like_button_clicked(request, quote_id):

    if request.user.is_authenticated():

        if not already_liked_quote(request.user, quote_id):
            Like.objects.create(user=request.user, quote_id=quote_id, timestamp=datetime.now())
        else:
            Like.objects.filter(user=request.user, quote_id=quote_id).delete()

        return redirect(reverse('index'))
    else:
        return redirect(reverse('login'))

def dashboard_add_quote(request, username):

    text = request.POST.get('quote')

    if text:
        # TODO: return visual feedback if quote already exists
        if not Quote.objects.filter(text=text):
            new_quote = Quote.objects.create(text=text, author=username, date=datetime.now())
            new_quote.save()


    return render(request, 'quotes/dashboard-add.html')
