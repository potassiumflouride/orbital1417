from django.shortcuts import render
from django.http import HttpResponse
from charity.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    post_list = Post.objects.all()
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

    return render(request, 'index_charity.html', context)
