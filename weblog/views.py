from django.http import HttpResponseRedirect
from django.shortcuts import render
from weblog.models import Post, Comment
from weblog.forms import CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def blog_index(request):

    posts = Post.objects.all().order_by("-created_on")

    context = {

        "posts": posts,

    }

    return render(request, "index.html", context)




def blog_category(request, category):

    posts = Post.objects.filter(

        categories__name__contains=category

    ).order_by("-created_on")

    context = {

        "category": category,

        "posts": posts,

    }

    return render(request, "category.html", context)





@login_required
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,  # Changed from "CommentForm()" to "form"
    }
    return render(request, "detail.html", context)


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False  # Set is_staff to False for regular users
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('blog_index')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('blog_index')


