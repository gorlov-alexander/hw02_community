from django.core.paginator import Paginator

from django.shortcuts import redirect, render, get_object_or_404

from .models import Group, Post, User

from .forms import PostForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = User.objects.get(username=username)
    post_list = Post.objects.filter(author=author)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'post_list': post_list,
        'author': author,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm()
        if form.is_valid():
            post_create = form.save(commit=False)
            post_create.author = request.user
            post_create.save()
            return redirect('posts:profile', usernane=request.user)
    else:
        form = PostForm(request.POST)
    context = {'form': form}
    return render(request, 'posts/post_create.html', context)


'''
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    is_edit = True
    form = PostForm(request.POST or None, instance=post)
    if request.user == post.author:
        return redirect('posts:post_detail', post_id)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)
    context = {
        'form': form,
        'post': post,
        'is_edit': is_edit,
    }
    return render(request, 'posts/create_post.html', context)'''