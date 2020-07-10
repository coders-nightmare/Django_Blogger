from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, BlogComment
from django.contrib import messages

# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    print(post)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/blogPost.html', context)


def postComment(request):
    if(request.method == "POST"):
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")
        post = Post.objects.get(sno=postSno)
        if(parentSno == ""):
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(
                request, "your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(
                request, "your reply has been posted successfully")
    return redirect(f'/blog/{post.slug}')
