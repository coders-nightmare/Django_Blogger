from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.


def home(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html', context)


def contact(request):
    messages.info(request, 'Welcome To contacts')
    if(request.method == 'POST'):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')
        if(len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 5):
            messages.error(request, "Please fill the form details correctly! ")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been Successfully sent")
    return render(request, 'home/contact.html')


def about(request):
    messages.success(request, 'Welcome To abouts')
    return render(request, 'home/about.html')
