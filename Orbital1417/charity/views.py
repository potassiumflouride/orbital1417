from django.shortcuts import render
from django.http import HttpResponse
from charity.models import Post




def index(request):
    post = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post = post.filter(title__icontains=query)

    context = {
    'post':post
    }
    return render(request, 'index.html', context)
