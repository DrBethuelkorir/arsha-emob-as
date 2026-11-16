from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .form import ContactForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'arsha/home.html')

def about(request):
    return render(request, 'arsha/about.html')

def services(request):
    return render(request, 'arsha/services.html')

def portfolio(request):
    return render(request, 'arsha/portfolio.html')

def portfolio_details(request):
    return render(request, 'arsha/portfolio_details.html')

def team(request):
    return render(request, 'arsha/team.html')

def pricing(request):
    return render(request, 'arsha/pricing.html')

def blog(request):
    return render(request, 'arsha/blog.html')

def blog_details(request):
    return render(request, 'arsha/blog_details.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'arsha/contact.html', {'form': form})
def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard_home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Invalid credentials or not authorized.')

    return render(request, 'arsha/dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ContactMessage

@login_required(login_url='dashboard_login')
def dashboard_home(request):
    # Security check: Only staff can see this
    if not request.user.is_staff:
        return HttpResponseForbidden('You do not have permission to view this page.')

    messages_qs = ContactMessage.objects.all()
    
    # We will pass the messages to the template
    context = {
        'messages_list': messages_qs
    }
    return render(request, 'arsha/dashboard/home.html', context)