from django.core.mail import send_mail
from chocolux.settings import EMAIL_HOST_USER
from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from .models import SocialLinks
from .forms import EmailForm
from .models import Chocolate

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def chocolate_view(request):
    chocolates = Chocolate.objects.all()
    return render(request, 'chocolate.html', {'chocolates': chocolates})

def testimonial_view(request):
    return render(request, 'testimonial.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('Test Subject',
                      'Size yeni muraciet gelmisdir.',
                      EMAIL_HOST_USER,
                      ['nerminyusifova1100@gmail.com'] )
            messages.success(request, "Your message has been sent successfully!")
        return redirect("chocoapp:contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form':form})

def footer_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            return render(request, 'footer.html', {'form': form, 'message': 'Email added successfully'})
    else:
        form = EmailForm()
    return render(request, 'footer.html', {'form': form})

def home(request):
    links = SocialLinks.objects.first()
    return render(request, "index.html", {"links": links})


