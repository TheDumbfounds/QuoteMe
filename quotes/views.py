from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import Quote, Like
from django.contrib.auth.models import User
from datetime import datetime
import json

def index(request):

    quotes = Quote.objects.all()

    if request.user.is_authenticated():
        liked_quote_ids = [x.quote_id for x in Like.objects.filter(user=request.user)]
    else:
        liked_quote_ids = []

    data = {'quotes': quotes, 'liked_quote_ids': liked_quote_ids}
    return render(request, 'quotes/index.html', data)

def dashboard(request, username):

    user = User.objects.get(username=username)
    liked_quotes = Like.objects.all().filter(user=user)

    liked_quote_ids = [x.quote_id for x in liked_quotes]
    liked_quotes = [x for x in Quote.objects.all() if x.id in liked_quote_ids]

    data = {'liked_quotes': liked_quotes, 'liked_quote_ids': liked_quote_ids}

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
