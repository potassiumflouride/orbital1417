# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, render_to_response

from django.template import RequestContext
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse

from userAcc.forms import SignUpForm
from userAcc.tokens import account_activation_token

from django.core.mail import EmailMessage
from django.http import HttpResponse




# Create your views here.
# main userAcc page to allow charity to post their job listing

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            '''
            current_site = get_current_site(request)
            subject = 'Activate Your orbital1417 Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            toemail=form.cleaned_data.get('email')
            # email = EmailMessage(subject, message, to=[toemail])

            sendHTMLEmail(request , toemail)

            return redirect('account_activation_sent')'''
            if user is not None:
                user.is_active = True
                user.profile.email_confirmed = True
                user.save()
                login(request, user)
                return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

'''
def sendHTMLEmail(request , emailto):
   html_content = "<strong>HUH-y Account Activation</strong>"
   email = EmailMessage("Account Activation", html_content, "orbital1417@gmail.com", [emailto])
   email.content_subtype = "html"
   res = email.send()
   return HttpResponse('%s'%res)

def account_activation_sent(request):

    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

        '''
