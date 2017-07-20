from django.shortcuts import render
from django.http import HttpResponse
from tracklah.models import CharPost
from tracklah.models import CharityProjects
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import simplejson
from django.core.serializers import serialize
import json


def index(request):
    #charpost
    post_list = CharPost.objects.all()
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


    #charityProjects
    CharityProjects_list= json.dumps(serializers.serialize('json',CharityProjects.objects.all()))






    """query = request.GET.get('q')
    if query:
        post_list = post_list.filter(title__icontains=query) #change here to change search value type
        context ={'post':post_list,
        'q':query
        }"""

    context = {
    'post':None,
    }

    query =  request.GET.get('q')
    if request.method == 'GET' and query: # this will be GET now
        try:
            post1 = CharPost.objects.filter(title__icontains=query)
        except:
            None # filter returns a list so you might consider skip except part
        if post1!=post_list:
            return render(request,'trackhome.html',{"post":post1, "CharityProjects_list":CharityProjects_list})
        else:
            return render(request,'trackhome.html',{"post":False, "CharityProjects_list":CharityProjects_list})
    else:
        return render(request,'trackhome.html',{"post":None, "CharityProjects_list":CharityProjects_list,})
