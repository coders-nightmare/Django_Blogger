from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Contact
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


def search(request):
    # allPosts = Post.objects.all()
    query = request.GET['query']
    if(len(query) > 75):
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if(len(allPosts) == 0):
        messages.warning(
            request, 'No search results founds. Please refine your query.')

    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


# handling sign up
def handleSignup(request):
    if(request.method == "POST"):
        username = request.POST.get('username', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        # Check for errorneous inputs
        if(len(username) > 10):
            messages.error(
                request, "Username must be under 10 Characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(
                request, "Username cannot contain special characters")
            return redirect('/')
        if(password1 != password2):
            messages.error(
                request, "Passwords are not matching")
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "Your Blogger account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


# handleing login
def handleLogin(request):
    if(request.method == "POST"):
        loginusername = request.POST.get('loginusername', '')
        loginpassword = request.POST.get('loginpassword', '')

        # authenticating
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully LoggedIn")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please Try again")
            return redirect('/')
    return HttpResponse("<h1>404 - Not Found</h1>")


# handleing logout
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully LoggedOut")
    return redirect('/')
