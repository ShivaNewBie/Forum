from django.shortcuts import render
from .models import *
# Create your views here.
def home_view(request):
    forumpost = ForumPost.objects.all()
    user = request.user
    context = {
        'forumpost': forumpost,
        'user': user
    }
    return render(request,'home.html',context)


def forum_post_view(request,id): #view individual user post
    forumpost = ForumPost.objects.get(id=id)
    context = {
        'forumpost': forumpost,
    }
    return render(request, 'forumpost/forumpostview.html', context)

def forum_page_view(request):
    return render(request, 'forum.html')

def forum_detail_view(request):
    return render(request,'forumpost/forumdetail.html')