from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from openai import OpenAI
from .models import Letter
import os

# Create your views here.
# these views here are just basic pageloading
def home(request):
    """ This is to navigate to home page """

    # get all letters for the home page made by current user - needs to change to all users created in the database
    try:
        letters = Letter.objects.select_related('user').all()
    except:
        return render(request, 'home.html')
    return render(request, 'home.html', {'letters': letters})

def dashboard(request):
    """ This is to navigate to dashboard """

    return render(request, 'dashboard.html')

def write_letter(request):
    # context = {}
    

    # if request.method == "POST":
    #     wishlist = request.POST.get("wishlist", "")
    #     letter = request.POST.get("letter", "")

    #     #no data base here, fake success
    #     context["success"] = True
    #     context["wishlist"] = wishlist
    #     context["letter"] = letter

    return render(request, "write_letter.html")

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



# May use these again if we decide to style all-auth pages
# def login(request):
#     return render(request, 'account/login.html')

# def signup(request):
#     return render(request, 'account/signup.html')

# def logout(request):
#     return render(request, 'account/logout.html')

# def change_password(request):
#     return render(request, 'account/password_change.html')

# def reset_password(request):
#     return render(request, 'account/password_reset.html')

# def complete_reset_password(request):
#     return render(request, 'account/password_reset_done.html')

# def email_management(request):
#     return render(request, 'account/email.html')

# def email_confirmation(request):
#     return render(request, 'account/email_confirm.html')