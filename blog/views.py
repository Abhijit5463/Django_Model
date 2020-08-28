
from django.shortcuts import render

posts = [
    {
        'author': 'BABA',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'August 26, 2020'
    },
    {
        'author': 'CM',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': 'August 26, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})