from django.shortcuts import render

# Create your views here.

def home(request):
    ctx = {
        'course': 'IT373 - Web Systems and Technologies 2',
        'week': '1',
    }
    return render(request, 'pages/home.html', ctx)

def hello(request):
    return render(request, 'pages/hello.html')

def about(request):
    return render(request, 'pages/about.html')

