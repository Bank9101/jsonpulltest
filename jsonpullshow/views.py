from django.shortcuts import render

# Create your views here.
def index(request):
    rendered = render(request, 'index.html')
    return rendered