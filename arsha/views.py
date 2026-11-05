from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'arsha/index.html')

def blog(request):
    return render(request, 'arsha/blog.html')