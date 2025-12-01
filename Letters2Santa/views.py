from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from openai import OpenAI
from .models import Letter
from django.http import JsonResponse
import random
import os

# Create your views here.
# these views here are just basic pageloading
def home(request):
    """ This is to navigate to home page """

    # get all letters for the home page made by current user - needs to change to all users created in the database
    try:
        letters = Letter.objects.all()
    except:
        return render(request, 'home.html')
    return render(request, 'home.html', {'letters': letters})

def dashboard(request):
    """ This is to navigate to dashboard """

    return render(request, 'dashboard.html')

def write_letter(request):
    """ for navigating to the write a letter page """

    return render(request, 'write_letter.html')

# This is for handling form request for letters and saving AI response 
@login_required
def send_letter(request):
    """ This is set up so we can send info to the AI via API and save the response in the same view """

    # lets collect form information when user sends letter to santa
    if request.method == 'POST':
        letter = request.POST.get('letter')
        wishlist = request.POST.get('wishlist')
        # connect to API client
        client = OpenAI(
            api_key = settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )
        # send data
        response = client.responses.create(
            # input=f'You have received a letter from someone who thinks you are santa. Read their letter and wish list. Give them a wholesome response! -  {letter} - {wishlist}',
            input=f'You have received a letter from someone who thinks you are santa. pretend you are drunk and not santa. Be casual and not innappropriate, be comedic about it. Also, no more than 100 characters output plz -  {letter} - {wishlist}',
            model="openai/gpt-oss-20b",
        )
        # Gather the response
        santas_response = response.output_text

        Letter.objects.create(
            user=request.user,
            letter=letter,
            wishlist=wishlist,
            response=santas_response
        )

    letters = Letter.objects.all()
    return render(request, 'home.html', {'letters': letters})

FESTIVE_MESSAGES = [
    "Have a magical day full of Christmas spirit! ✨",
    "May your day be merry and bright. 🎄",
    "Don’t forget to treat yourself today – Santa is watching. 🎅",
    "One hot chocolate a day keeps the Grinch away. ☕",
]

def festive_message_api(request):
    message = random.choice(FESTIVE_MESSAGES)
    return JsonResponse({"message": message})

# May use these again if we decide to style all-auth pages
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ChangePasswordForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                auth_login(request, user)
                return redirect('home.html')
    else:
        form = LoginForm(request=request)
    return render(request, 'account/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        if form.is_valid():
            user = form.save(request)
            auth_login(request, user)
            return redirect('home.html')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

def logout(request):
    return render(request, 'account/logout.html')

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home.html')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'account/password_change.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST or None)
        if form.is_valid():
            form.save(request)
            return redirect('home.html')
    else:
        form = ResetPasswordForm()
    return render(request, 'account/password_reset.html', {'form': form})

def complete_reset_password(request):
    return render(request, 'account/password_reset_done.html')

def email_management(request):
    return render(request, 'account/email.html')

def email_confirmation(request):
    return render(request, 'account/email_confirm.html')