from django.shortcuts import render

def index(request) :
    context = {
        'judul' : 'Kabs Learning',
    }
    return render(request, 'index.html', context)