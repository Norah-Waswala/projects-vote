from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, PostForm, DetailsForm,UpdateUserForm, UpdateUserProfileForm, RatingsForm
from rest_framework import viewsets
from .models import Profile, Post, Rating
from .serializers import ProfileSerializer, PostSerializer
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView



def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("index")
    return render(request,'registration/login.html')
def register(request):
    if request.method == "POST":
        username=request.POST["username"]
       
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('registration/register')
        new_user=User.objects.create_user(
            username=username,
           
            email=email,
            password=password1,
        )
        new_user.save()
        return render (request,'registration/login.html')
    return render(request,'registration/signup.html')

def signout(request):
    logout(request)
    return render(request,'index.html')

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all()
    current_user = request.user.username 
    
    if request.method=='POST':
        
        details_form = DetailsForm(request.POST, request.FILES)
        posts_form = PostForm(request.POST, request.FILES)
        
        if details_form.is_valid():
            profile = details_form.save(commit=False)
            profile.user = current_user
            profile.save()
            
        if posts_form.is_valid():
            post = posts_form.save(commit=False)
            post.user = current_user
            posts_form.save()
            
        return redirect('index')
        
    else:
        details_form = DetailsForm
        posts_form = PostForm
        
    return render(request,'index.html', { 'details_form':details_form,'posts_form':posts_form, 'posts':posts,})






def profile(request,username):
   
    user=User.objects.get(username=username)
    posts=Post.objects.filter(user=user.id)
  
    return render(request, 'profile.html',{'posts':posts,'user':user})





@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit.html', params)


@login_required(login_url='login')
def project(request, post):
    post = Post.objects.get(title=post)
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'single.html', params)


def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Post.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)