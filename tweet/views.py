 
 
from django.shortcuts import render
from .models import Profile, Tweet
from .forms import tweetForm
from .forms import ProfileForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm
# home view
def index(request):
    return render(request ,'index.html')

#user profile
 

@login_required
def user_profile(request):
    profile,created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'user_profile.html', {'profile': profile})
 
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})



# list of tweets view0
@login_required
def Tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

# create tweet

@login_required
def tweet_create(request):
    # if form have post method
    if request.method=='POST':
        form=tweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)  #"commit=False is use to not save data in DB for certain time"
            tweet.user=request.user
            tweet.save()
            return redirect("Tweet_list")
    # if empty form         
    else:
        form=tweetForm()
    return render(request,'tweet_form.html',{'form':form})

# To Edit the tweet 
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id ,user=request.user)  # Fetch the existing tweet
    
    if request.method == 'POST':
        form = tweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('Tweet_list')  # Redirect after saving
    else:
        form = tweetForm(instance=tweet)  # Assign form for GET request

    return render(request, 'tweet_form.html', {'form': form})

#  to delete
@login_required
def  tweet_delete(request ,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect("Tweet_list")
    return render(request,"tweet_confirm_delete.html",{'tweet':tweet})

def register(request):
    if  request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('Tweet_list')
    else:
        form=UserRegistrationForm()
    return render(request ,'registration/register.html',{'form': form})
