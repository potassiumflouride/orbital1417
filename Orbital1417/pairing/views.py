# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,render_to_response

from django.http import HttpResponse

from django.shortcuts import render

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect

from pairing.forms import PairingSignupform

from userAcc.forms import SignUpForm

from django.contrib.auth.decorators import login_required

from pairing.models import Pairing

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# main pairing page to allow charity to post their job listing
def pairingPost(request):

    #post = Pairing.objects.all()

    #query = request.GET.get('q')
    #if query:
        #post = post.filter(title__icontains=query)

    #context = {
    #'post':post
    #}

    post_list = Pairing.objects.all()
    paginator = Paginator(post_list, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)

    context = {
    'post':post
    }

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(title__icontains=query)
        context ={'post':post_list
        }

    return render(request, 'pairingPage.html', context)

@login_required
def pairingSignUp(request):
    if request.method== 'POST':
        form= PairingSignupform(request.POST)
        print("form object created")

        if form.is_valid():
            print("inputs validated")
            form.save()
            return redirect('/pairing/')
    else:
        form= PairingSignupform()
    return render(request,'pairingform.html', {'pairingSignupform':form})

    '''
    if request.user.is_authenticated():  #if user is already logined
        return HttpResponseRedirect('/$')
    if request.method == 'POST'         #if user is attempting to login
        form= login()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(username = username, password=password)

            if user is not None:            #if user login parameters are correct
                login(request, user)
                return HttpResponseRedirect('/$')
            else:
                return render_to_response('userAcc/signup.html', {'form': form},  context_instance = RequestContext(request))
        else:
            return render_to_response('userAcc/signup.html', {'form': form},  context_instance = RequestContext(request))

    else:
        return render_to_response('userAcc/signup.html', {'form': form},  context_instance = RequestContext(request))
'''
