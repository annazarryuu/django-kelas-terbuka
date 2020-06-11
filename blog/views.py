from django.shortcuts import render

# Create your views here.

def index(request) :
    context = {
        'judul' : 'Blog',
        'sub_judul' : 'Ini blog loh, kamu tau ngga?',
        'app_css' : 'blog/css/styles.css',
    }
    return render(request, 'blog\\index.html', context)