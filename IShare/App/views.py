from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from datetime import datetime


def index(request):  # Render Landing Page for unauthenticated user
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'App/index.html')


def signup(request):  # Sign Up Page
    if request.user.is_authenticated:  # no need to register again if user already exist
        return redirect('dashboard')
    else:
        # form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                # if form.username.exist():

                user = form.save()
                login(request, user)
                return redirect('dashboard')
        else:
            form = RegisterForm()

    # context = {'form': form}
    return render(request, 'App/signup.html', {'form': form})


def loginpage(request):
    if request.user.is_authenticated:  # no need to register again if user already exist
        return redirect('dashboard')
    else:
        form = RegisterForm()
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form = RegisterForm()
    context = {'form': form}
    return render(request, 'App/login.html', context)


def logoutUser(request):  # Logout logic
    logout(request)
    return redirect('/')


# redirect when user is not logged in
@login_required(login_url='login')
def dashboard(request):  # Main dashboard
    newpost = Post.objects.all().order_by('-createdTime')

    if request.method == "POST" and 'newpost' in request.POST:
        newdata = request.POST.get('newpost')
        username = request.user
        createdTime = datetime.now()
        newdata = str(newdata).strip()
        if not newdata:
            return HttpResponse("Post data cannot be empty", 405)
        # if str(newdata).strip()
        newpost = Post(username=username, postData=newdata,
                       createdTime=createdTime)
        newpost.save()
        return redirect('dashboard')

    if request.method == 'POST' and 'newComment' in request.POST:
        # print(f":::post data ={request.POST}")
        post_id = int(request.POST.get('post_id'))
        newComment = request.POST.get('newComment')
        username = request.user
        postID = Post.objects.get(pk=post_id)
        # print(username, postID, newComment)
        commentTime = datetime.now()

        comments = LikeComment(username=username, postID=postID,
                               commentData=newComment, commentTime=commentTime)

        comments.save()
    user = User.objects.all()
    comments = LikeComment.objects.all()
    context = {
        'user': user,
        'newpost': newpost,
        'comments': comments
    }
    return render(request, 'App/dashboard.html', context)


@login_required(login_url='login')
def profile(request):
    context = {}
    user = User.objects.get(id=request.user.id)
    if request.method == "POST" and 'newpost' in request.POST:
        newdata = request.POST.get('newpost')
        username = request.user
        createdTime = datetime.now()
        newdata = str(newdata).strip()

        newpost = Post(username=username, postData=newdata,
                       createdTime=createdTime)
        newpost.save()
        # return render(request, 'App/profile.html', context)

    try:
        data = UserDetail.objects.get(username=request.user.id)
        if request.method == "POST":
            data.about = request.POST.get('about')
            data.job = request.POST.get('job')
            data.address = request.POST.get('address')
            data.phone = request.POST.get('phone')
            data.githubProfile = request.POST.get('githubProfile')
            data.linkedinProfile = request.POST.get('linkedinProfile')
            data.save()

            username = request.POST.get('username')
            user.first_name = username
            user.save()

    except UserDetail.DoesNotExist:
        data = {}
        if request.method == "POST":
            username = request.POST.get('username')
            about = request.POST.get('about')
            job = request.POST.get('job')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            githubProfile = request.POST.get('githubProfile')
            linkedinProfile = request.POST.get('linkedinProfile')

            data = UserDetail(username=request.user, about=about, job=job, address=address, phone=phone,
                              githubProfile=githubProfile, linkedinProfile=linkedinProfile)
            data.save()
            user.first_name = username
            user.save()

    newpost = Post.objects.filter(
        username=request.user.id).order_by('-createdTime')
    context = {
        'data': data,
        # 'user': user,
        'newpost': newpost
    }
    return render(request, 'App/profile.html', context)


@login_required(login_url='login')
def updatePost(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user.id != post.username.id:
        return redirect('dashboard')
    if request.method == "POST":
        newdata = request.POST.get('newpost')
        post.postData = newdata
        post.save()
        return redirect('dashboard')

    context = {'newpost': post}
    return render(request, 'App/updatePost.html', context)


@login_required(login_url='login')
def delete_event(request, event_id):
    event = Post.objects.get(pk=event_id)
    if request.user.id == event.username.id:
        event.delete()
    return redirect('dashboard')


@login_required(login_url='login')
def commentPost(request, post_id):
    user = User.objects.all()
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        newComment = request.POST.get('newComment')
        username = request.user
        postID = Post.objects.get(pk=post_id)
        print(username, post.id, newComment)
        commentTime = datetime.now()

        comments = LikeComment(username=username, postID=postID,
                               commentData=newComment, commentTime=commentTime)

        comments.save()

        # return redirect('/')
    comments = LikeComment.objects.all().order_by('-commentTime')

    context = {
        'comments': comments,
        'post': post,
        'user': user,
    }
    return render(request, 'App/commentPost.html', context)


def error404_template(request, exception):
    return render(request, 'App/error404_template.html', status=404)


def notification(request):
    return render(request, 'App/notification.html')


def challange(request):
    return render(request, 'App/challange.html')


def frequently(request):
    return render(request, 'App/frequently.html')


def roadmap(request):
    return render(request, 'App/roadmap.html')


def about(request):
    return render(request, 'App/about.html')


def help(request):
    return render(request, 'App/help.html')


def test(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    return render(request, 'App/test.html', context)
