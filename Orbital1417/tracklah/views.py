from django.shortcuts import render
from django.http import HttpResponse
from tracklah.models import CharPost
from tracklah.models import CharityProjects
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import simplejson
import json
from django.shortcuts import render



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

    CharityProjects_list= serializers.serialize("json",CharityProjects.objects.all())
    allCharPost_list = serializers.serialize("json",CharPost.objects.all())
    #CharityProjects_list= json.dumps(CharityProjects.objects.all())
    #print(CharityProjects_list)

    """query = request.GET.get('q')
    if query:
        post_list = post_list.filter(title__icontains=query) #change here to change search value type
        context ={'post':post_list,
        'q':query
        }"""

    '''context = {
    'post':None,
    }'''
    '''
    query =  request.GET.get('q')
    if request.method == 'GET' and query: # this will be GET now
        try:
            post1 = CharPost.objects.filter(title__iexact=query)
            mapquery=CharityProjects_list.objects.filter(chocoCode_iexact=query)

        except:
            None # filter returns a list so you might consider skip except part
        if post1!=post_list:
            return render(request,'trackhome.html',{"post":post1, "CharityProjects_list":mapquery} )
        else:
            return render(request,'trackhome.html',{"post":False, "CharityProjects_list":mapquery)
    else:
        return render(request,'trackhome.html',{"post":None, "CharityProjects_list":mapquery}) '''



    query =  request.GET.get('q')
    if request.method == 'GET' and query: # this will be GET now
        post1 = CharPost.objects.filter(title__iexact=query)

        if post1 is post_list:
            return render(request,'trackhome.html',context={"allCharPost_list": allCharPost_list,"post":False, "CharityProjects_list":CharityProjects_list} )
        else:
            return render(request,'trackhome.html',context= {"allCharPost_list": allCharPost_list, "post":post1, "CharityProjects_list":CharityProjects_list})
    else:
        return render(request, 'trackhome.html', context= {"allCharPost_list": allCharPost_list,"post":None, "CharityProjects_list":CharityProjects_list})
