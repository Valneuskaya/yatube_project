from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    context = {
       'posts': posts,
       'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    context = {
       'group': group,
       'posts': posts,
       'title': title,
    }
    return render(request, template, context)
