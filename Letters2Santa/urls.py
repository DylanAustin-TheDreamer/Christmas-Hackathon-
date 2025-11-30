from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path("write-letter/", views.write_letter, name="write_letter"),
    path('send-letter/', views.send_letter, name="send_letter"),
]