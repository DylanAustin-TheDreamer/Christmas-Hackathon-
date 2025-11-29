from django.shortcuts import render

# Create your views here.
# of these views here are just basic pageloading
def home(request):
    letters = range(6)  # Fake 6 letters for display purposes
    return render(request, "home.html", {"letters": letters})

def dashboard(request):
    return render(request, 'dashboard.html')


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