from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

from .forms import PostForm,LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate

# posts = [
#     {
#         'title': 'Beautiful is better than ugly',
#         'author': 'John Doe',
#         'content': 'Beautiful is better than ugly',
#         'published_at': 'October 1, 2022'
#     },
#     {
#         'title': 'Explicit is better than implicit',
#         'author': 'Jane Doe',
#         'content': 'Explicit is better than implicit',
#         'published_at': 'October 1, 2022'
#     }
# ]

@login_required
def delete_post(request,id):
    queryset = Post.objects.filter(author=request.user)

    post= get_object_or_404(Post, pk=id)
    context={'post':post}

    if request.method == 'GET':
        return render(request,'users/post_delete.html',context)
    elif request.method =='POST':
        post.delete()
        messages.success(request,'The post has been deleted successfully.')
        return redirect('posts')

    

@login_required
def edit_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post=get_object_or_404(Post,id=id)

    if(request.method=='GET'):
        context={'form':PostForm(instance=post),'id':id}
        return render(request,'users/post_form.html',context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'users/post_form.html',{'form':form})

# def login(request):
#     if request.method == "GET":
#         form=LoginForm()
#         return render(request,'users/login.html')
    
#     elif request.method == "POST":
#         print(request.POST)
#         return HttpResponse("ybguivf")
    


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request,'users/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'users/post_form.html',{'form':form})  

def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'users/home.html',context)

def about(request):
    return render(request,'users/about.html')


# Create your views here.
