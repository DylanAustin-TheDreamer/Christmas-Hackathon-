from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('write-letter', views.write_letter, name="write_letter"),
    path('send-letter/', views.send_letter, name="send_letter"),
    path("api/festive-message/", views.festive_message_api, name="festive_message_api"),
    path('password-change/', views.change_password, name='password_change'),
    path('password-reset/', views.reset_password, name='password_reset'),
    path('password-reset/done/', views.complete_reset_password, name='password_reset_done'),
    path('email/', views.email_management, name='email_management'),
    path('email-confirmation/', views.email_confirmation, name='email_confirmation'),
]