from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': "ArmenG",
        'title': 'My photo',
        'content': 'bwoah',
        'data_posted':'June 10, 2777'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'social_media/home.html',context)
    
