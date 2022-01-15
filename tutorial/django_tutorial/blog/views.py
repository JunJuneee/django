from django.shortcuts import render

posts = [
    {
        'author': 'nana',
        'title': 'blog 1',
        'content': 'first content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'nunu',
        'title': 'blog 2',
        'content': '2 content',
        'date_posted': 'August 27, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
