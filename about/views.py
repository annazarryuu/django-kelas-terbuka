from django.shortcuts import render

# Create your views here.

def index(request) :
    context = {
        'judul' : 'About',
        'sub_judul' : 'Di sini tuh about, jangan nyasar yaa.',
        'app_css' : 'about/css/styles.css',
    }
    return render(request, 'about\\index.html', context)