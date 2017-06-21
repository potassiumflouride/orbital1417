from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from userAcc import views as userAcc_views


urlpatterns = [

    url(r'^$', userAcc_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', userAcc_views.signup, name='signup'),
    #url(r'^account_activation_sent/$', userAcc_views.account_activation_sent, name='account_activation_sent'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #userAcc_views.activate, name='activate'),

]
