from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
# Create your views here.


def posts(request):
    post_list = Post.objects.all()
    return render(request, 'rich_text_editor_learning/posts.html', {'posts': post_list})


def add_view(request):
    if request.method == 'GET':
        # create form
        form = PostForm()
        return render(request, 'rich_text_editor_learning/new_post.html', {'form': form})

    else:
        # create model
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('rich_text_editor_learning:posts')


def update_post(request):
    if request.method == 'POST':
        # get object
        id = request.POST.get('id')
        post = Post.objects.get(pk=id)

        # update model
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

        return redirect('rich_text_editor_learning:posts')

    else:
        # get object
        id = request.GET.get('id')
        post = Post.objects.get(pk=id)

        # create form
        form = PostForm(instance=post)
        return render(request, 'rich_text_editor_learning/post.html', {'form': form})
