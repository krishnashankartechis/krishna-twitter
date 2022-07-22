from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 





from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse #A!
from cloudinary.forms import cl_init_js_callbacks #A!
# Create your views here.


def index(request):
    # return HttpResponse("hello")
    # return render(request,'posts.html')
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
           # if yes save it and redirect it to home
            return HttpResponseRedirect('/')

        # if no then show error
        else:
            return HttpResponseRedirect(form.errors.as_json())  #changed from erros ot errors

    # posts = Post.objects.all()[:20]      it works like pop
    posts = Post.objects.all().order_by('-created_at')[:20] #A!
    return render(request,'posts.html',{'posts':posts }) 

def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


#####A!#########################################


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:

            return HttpResponseRedirect(form.erros.as_json())
    return render(request, "edit.html", {"post": post})


def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
