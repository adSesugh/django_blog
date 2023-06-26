from django.shortcuts import render, redirect
from posts.models import Post
from django.utils import timezone

def home(request):
    posts = Post.objects.all().values()
    context = {
        'posts': posts
    }
    return render(request, 'post/list.html', context)


def create_post(request):
    return render(request, 'post/create.html', {})

def save_post(request):
    
    if request.method == 'POST':
             
        post = Post.objects.create(
            title = request.POST['title'], 
            content =request.POST['content'],
            published = True if request.POST['published'] == 'on' else False,
            #published_at = timezone.now() if request.POST['published'] == 'on' else None 
        )
        
        if post:
            return redirect('posts')
        
    return render(request, 'post/create.html', {})

# view function coupling (save and render form function)
# def create_new(request):
#     if request.method == 'POST':
#         post = Post.objects.create(
#             title = request.POST['title'], 
#             content =request.POST['content'],
#             published = True if request.POST['published'] == 'on' else False,
#             published_at = timezone.now() if request.POST['published'] == 'on' else None 
#         )
        
#         if post:
#             return redirect('posts')
        
    
#     return render(request, 'post/create.html', {})

def get_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'post/detail.html', {'post': post})

def publish_switch(request, id):
    post = Post.objects.get(pk=id)
    post.published = not post.published
    post.save()
    
    return redirect('posts')


def post_edit(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'post/edit.html', {'post': post})

def post_update(request, id):
    post = Post.objects.get(pk=id)
    if post:
        post.title = request.POST['title'], 
        post.content =request.POST['content'],
        
        post.save()
        
        return redirect('posts')
    
    return render(request, 'post/edit.html', {'post': post})


def post_delete(request, id):
    post = Post.objects.get(pk=id)
    if post:
        post.delete()
        
        return redirect('posts')
    
    return redirect('posts')
    
    