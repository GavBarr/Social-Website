from django.shortcuts import render
from .models import Profile, UserNote, UserPost, UserFollower, UserFollowing
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, ProfileForm, AddNoteForm, AddPostForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.db.models import F
from django.db.models import Q
from django.contrib.auth.models import User
from django import forms
# Create your views here.


def search(request):
    query = request.GET.get('q')
    if query:
        results = User.objects.filter(Q(username__icontains=query))
    else:
        results = []
    return render(request, 'socialapp/search.html', {'results': results, 'query': query})


@login_required
def view_profile(request, profile_id):
    temp_user = User.objects.get(pk=profile_id)
    profile_name = temp_user.username
    profile = Profile.objects.filter(username=profile_name)

    for p in profile:
       # print(p.user_id)
        notes = UserNote.objects.filter(user_id=p.id)
        posts = UserPost.objects.filter(user = p.user)
        user_followings = UserFollowing.objects.filter(user=p.user).count()
        user_followers = UserFollower.objects.filter(user=p.user).count()
        user_followings_object = UserFollowing.objects.filter(user=request.user.username)

    print("test")
    for test in user_followings_object:
        print(test.user)




    return render(request, 'socialapp/view_profile.html',
                  {"profile": profile, "notes": notes, "posts": posts, "user_followings": user_followings,
                   "user_followers": user_followers, "user_followings_object": user_followings_object})


@login_required
def profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    #print(profile_id)
    notes = UserNote.objects.filter(user_id=profile_id)
    posts = UserPost.objects.filter(user = request.user)
    user_followings = UserFollowing.objects.filter(user=request.user).count()
    user_followers = UserFollower.objects.filter(user=request.user).count()


    return render(request, 'socialapp/main_profile.html',
                  {"profile": profile, "notes": notes, "posts": posts, "user_followings": user_followings,
                   "user_followers": user_followers})


@login_required
def add_post(request, profile_id):
    postform = AddPostForm(request.POST or None)
    if postform.is_valid():
        postform.instance.user = request.user
        postform.instance.post_likes = 1
        postform.instance.post_dislikes = 1
        #print(postform.instance.user)  # debug line
        postform.save()
        return redirect('profile', profile_id)

    return render(request, 'socialapp/add_post.html', {'postform': postform,'profile': profile})


@login_required
def delete_post(request, post_id, profile_id):
    post = UserPost.objects.get(pk=post_id)
    post.delete()
    return redirect('profile', profile_id) #this needs to change to main_profile, when i can figure otu how to fix the logic


@login_required
def follow_profile(request, follow_profile_id, follow_profile_name):
    user_follower = UserFollower()
    user_following = UserFollowing()
    profile = Profile.objects.get(pk=follow_profile_id)

    user_follower.user = profile.user
    user_follower.follower = request.user.username
    user_follower.save()

    user_following.user = request.user.username
    user_following.following = profile.user
    user_following.save()
    results = User.objects.filter(username=profile.username)

    for r in results:
        temp_id = r.id


    return redirect('view_profile', temp_id)



@login_required
def unfollow_profile(request, follow_profile_id, follow_profile_name):

    profile = Profile.objects.get(pk=follow_profile_id)
    print(follow_profile_name)
    user_follower = UserFollower.objects.get(user=follow_profile_name)
    user_follower.delete()
    user_following = UserFollowing.objects.get(user=request.user.username)
    user_following.delete()

    results = User.objects.filter(username=profile.username)

    for r in results:
        temp_id = r.id


    return redirect('view_profile', temp_id)



@login_required
def like_post(request, post_id, profile_id):
    posts = UserPost.objects.all()#order_by('?')
    post = UserPost.objects.get(pk=post_id)
    post.post_likes += 1
    post.save()

    return render(request, 'socialapp/explore_page.html', {'posts': posts, 'profile': profile})



@login_required
def dislike_post(request, post_id, profile_id):
    posts = UserPost.objects.all()#.order_by('?')
    post = UserPost.objects.get(pk=post_id)
    post.post_dislikes += 1
    post.save()

    return render(request, 'socialapp/explore_page.html', {'posts': posts, 'profile': profile})


@login_required
def like_post_profile(request, post_id, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    print(profile.username)
    results = User.objects.filter(username=profile.username)

    for r in results:
        temp_id = r.id

    print(temp_id)
    post = UserPost.objects.get(pk=post_id)
    post.post_likes += 1
    post.save()

    return redirect('view_profile', temp_id) #this needs to change to main_profile, when i can figure otu how to fix the logic



@login_required
def dislike_post_profile(request, post_id, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    print(profile.username)
    results = User.objects.filter(username=profile.username)

    for r in results:
        temp_id = r.id

    print(temp_id)
    post = UserPost.objects.get(pk=post_id)
    post.post_dislikes += 1
    post.save()

    return redirect('view_profile',
                    temp_id)  # this needs to change to main_profile, when i can figure otu how to fix the logic


@login_required
def delete_note(request, note_id, profile_id):
    note = UserNote.objects.get(pk=note_id)
    note.delete()
    return redirect('profile', profile_id) #this needs to change to main_profile, when i can figure otu how to fix the logic

@login_required
def add_note(request, profile_id):
    form = AddNoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile', profile_id)

    return render(request, 'socialapp/add_note.html', {"form": form })


@login_required
def edit_note(request, note_id, profile_id):
    note = UserNote.objects.get(pk=note_id)
    form = AddNoteForm(request.POST or None, instance=note)
    form.user = request.user
    if form.is_valid():
        form.user = request.user
        form.save()
        return redirect('profile', profile_id)

    return render(request, 'socialapp/add_note.html', {"form": form })


@login_required
def profile_settings(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    form = ProfileForm(request.POST or None, instance=profile)
   # form.fields['username'].initial = request.user.username
    if form.is_valid():
        form.instance.username = request.user.username

        form.save()
        return redirect('profile', profile_id)

    return render(request, 'socialapp/profile_settings.html', {'form': form, 'profile': profile })


class CreateItem(CreateView):
    model = UserNote
    fields = ['user', 'note_header', 'note_detail']
    template_name = 'socialapp/add_note.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



def welcome_page(request):
    return render(request, 'socialapp/welcome_page.html')


@login_required
def post_feed(request, profile_id):
    posts = UserPost.objects.all()  # .order_by('?')

    profile = Profile.objects.get(pk=profile_id)
    user_following = UserFollowing.objects.filter(user = request.user)
    print(request.user)
    return render(request, 'socialapp/post_feed.html', {'posts': posts, 'profile': profile, "userfollowing":user_following})


@login_required
def explore_page(request, profile_id):
    posts = UserPost.objects.all()#.order_by('?')
    print(request.user.id)
    profile = Profile.objects.get(pk=profile_id)
    return render(request, 'socialapp/explore_page.html', {'posts': posts, 'profile': profile})





#@login_required
#def profile_settings(request):
 #   profiles = Profile.objects.all()
  #  return render(request, 'socialapp/main_profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('welcome_page',)
    else:
        form = RegistrationForm()
    return render(request, 'socialapp/register.html', {'form': form})


#def login(request):
  #  if request.method == 'POST':
    #    form = LoginForm(request.POST)
     #   if form.is_valid():
       #     form.save()
      #      username = form.cleaned_data.get('username')
       #     messages.success(request, f'Welcome {username}! You are logged in!')
       #     return redirect('profile user.profile.id')
  #  else:
    #    form = RegistrationForm()
  #  return render(request, 'socialapp/login.html', {'form': form})

