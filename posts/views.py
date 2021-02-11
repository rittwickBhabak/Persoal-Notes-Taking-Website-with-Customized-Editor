from django.shortcuts import render, redirect 
from django.contrib import messages
from posts.models import Post 
from posts.forms import PostForm, TagForm
# Create your views here.
def index(request):
    posts = Post.objects.all()
    my_list = []
    for post in posts:
        tags = post.tags.all()[:5]
        my_list.append({'post': post, 'tags': tags})
    context = {
        'posts': my_list
    }
    return render(request, 'posts/index.html', context)

def addnew(request):
    # try:
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            post_id = Post.objects.order_by('-id')[0].id 
            messages.success(request, f"New Post with id {post_id} added successful")
            return redirect(f'/posts/details/{post_id}')
    return render(request, 'posts/addpost.html', { 'form':form })
    # except Exception as e:
    #     messages.warning(request, f'{str(e)} Some error occoured')
    #     return redirect('/')

def postupdate(request, pk):
    form = PostForm()
    post = Post.objects.get(pk=pk)
    if post:
        form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST' and post is not None:
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, f"Post updated")
            path = '/'.join(['', 'posts', 'details', str(post.pk)])
            return redirect(path)
    return render(request, 'posts/addpost.html', { 'form':form })

def addtag(request):
    form = TagForm()

    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, f"New tag added successful")
            return redirect('/')
    return render(request, 'posts/addtag.html', { 'form':form })

def category(request, cat):
    posts = Post.objects.filter(tags__tag=cat)
    my_list = []
    for post in posts:
        tags = post.tags.all()[:5]
        my_list.append({'post': post, 'tags': tags})
    context = {
        'heading': f"Category: {cat}",
        'posts': my_list
    }
    return render(request, 'posts/index.html', context)

def search(request):
    query = request.GET.get('q').split()
    posts = Post.objects.filter(pk='-1')
    for q in query:
        posts = posts | Post.objects.filter(title__icontains=q)
        posts = posts | Post.objects.filter(description__icontains=q)
    my_list = []
    for post in posts:
        tags = post.tags.all()[:5]
        my_list.append({'post': post, 'tags': tags})
    context = {
        'posts': my_list,
        'heading': f"Search results for \"{' '.join(query)}\""
    }
    return render(request, 'posts/index.html', context)

def postdetails(request, pk):
    post = Post.objects.get(pk=pk)
    if post:
        context={
            'post': post 
        }
        return render(request, 'posts/postdetails.html', context)
    messasges.warning(request, 'Post not found')
    return redirect('/')

def postdelete(request, pk):
    if request.method=='POST':
        post = Post.objects.get(pk=pk)
        if post:
            post.delete()
            messages.success(request, 'Post deleted successfully')
            return redirect('/')
        messages.warning(request, 'Post not found')
        return('/')
    messages.warning(request, 'Method not allowed')
    return redirect('/')
