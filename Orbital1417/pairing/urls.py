
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from pairing import views as pairing_views


urlpatterns = [

    url(r'^$',pairing_views.pairing, name='pairing'), #landing page for pairing, with details for charity job listing
    url(r'^$', pairing_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', pairing_views.signup, name='signup'),
    url(r'^account_activation_sent/$', pairing_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        pairing_views.activate, name='activate'),
]
