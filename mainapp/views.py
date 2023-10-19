from django.shortcuts import render
from .models import Post,Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
def home(request):
    posts = Post.objects.all().order_by('-date_added')
    return render(request,"home.html",{
        "posts":posts,
    })
# Create your views here.

def comment_page(request):
    comments = Comment.objects.all().order_by('-date_added')
    if request.method == "POST" :
        cmtname = request.POST['commentname']
        cmtbody = request.POST['commentbody']
        cmtdata= Comment(name_id=cmtname,body=cmtbody)
        cmtdata.save()
        return HttpResponseRedirect('/comment_page?submitted=True')
    return render(request,"comment_page.html",{
        'comments':comments
    })