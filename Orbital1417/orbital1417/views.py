# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render




# Create your views here.
# main pairing page to allow charity to post their job listing
def homePage(request):
    return render(request, 'homepage.html')
