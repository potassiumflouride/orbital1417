from django.shortcuts import render
from django.http import HttpResponse
from charity.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1) # Show 25 contacts per page
    userInput = False;

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
    'post':post,
    'userInput': userInput,
    }

    query = request.GET.get('q')
    userInput = True;

    if query:
        try:
            post_list = post_list.get(title__icontains=query)
        except:
            userInput=1;
            context ={'post':None,
                      'userInput': userInput,
                            }
        else:
            context ={'post':post_list,
                    'userInput': userInput,
                            }

    return render(request, 'index_charity.html', context)
