from django.shortcuts import render, redirect
from .models import Artwork
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery_view(request):
    tag = request.GET.get('tag')
    sort = request.GET.get('sort', 'latest')
    
    artwork = Artwork.objects.all()
    
    if tag:
        artwork = artwork.filter(tag=tag)
        
    if sort == 'oldest':
        artwork = artwork.order_by('created_at')
    else:
        artwork = artwork.order_by('-created_at')
        
    return render(request, 'artwork.html', {'artwork': artwork, 'active_tag': tag})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'New Contact Form Message from {name}'
        full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        send_mail(
            subject,
            full_message,
            email,
            ['gauranshivarshney@ms.du.ac.in'],
            fail_silently=False
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')
    return render(request, 'contact.html')