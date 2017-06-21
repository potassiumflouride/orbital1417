
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from pairing import views as pairing_views



urlpatterns = [

    url(r'^$',pairing_views.pairingPost, name='pairingPost'), #landing page for pairing, with details for charity job listing

    url(r'^signUp/$',pairing_views.pairingSignUp, name='pairingSignUp'),
]
