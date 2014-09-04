from django.shortcuts import render

def home_page(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def contacts(request):
    return render(request, 'blog/contacts.html')

def publications(request):
    return render(request, 'blog/publications.html')
