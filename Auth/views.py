from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_user
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from Posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Notification
from django.core.mail import EmailMultiAlternatives


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('feeds')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')



                subject, from_email, to = 'Welcome to pixie!!!', 'pixie.social.official@gmail.com', email
                
                text_content = f"Hey {username}, Welcome to pixie, the social app. Pixie lets you express yourself to the world in the form of pixels. You can share your pics publicly to the whole world, explore the tags and make new friends. So lets get started!!! Thanking you, Pixie"
                
                html_content = f"<p>hey <strong>{username}</strong>,</p> <p>Welcome to pixie, the social app. Pixie lets you express yourself to the world in the form of pixels. You can share your pics publicly to the whole world, explore the tags and make new friends. So lets get started!!!</p> <p>Thanking you,<br>Pixie</p>"
                
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                


                user = authenticate(username=username, password=password)
                login(request, user)


                messages.success(request, f"Hey {username}, welcome to pixie! Now your account is create!!! So let's get started by following some user. ")
                
                return redirect('explore')
        else:
            form = UserRegisterForm()
        return render(request, 'Auth/register.html', {'form': form})

@login_required
def logout(request):
    messages.success(request, f'Alright {request.user.username}, you are successfully logged out!')
    logout_user(request)
    return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': "Profile",
        'posts': Post.objects.filter(author = request.user),
        'all_posts': Post.objects.all()
    }

    return render(request, 'Auth/profile.html', context)


@login_required
def user_detail(request, pk):
    target_user = User.objects.get(id=pk)
    if target_user != request.user:
        context = {
            'target_user': target_user,
            'posts': Post.objects.filter(author = target_user),
            'title': "User-details",
            'Home': 'active_link'
        }
        return render(request, 'Auth/user_details.html', context)
    else:
        return redirect('profile')


@login_required
def follow(request, pk):
    target_user = User.objects.get(id=pk)
    follower = request.user

    if target_user != follower:
        if follower in target_user.profile.followers.all():
            target_user.profile.followers.remove(follower)
            follower.profile.following.remove(target_user)
        else:
            target_user.profile.followers.add(follower)
            follower.profile.following.add(target_user)

        return redirect('user_detail', pk=target_user.id)

    else:
        return redirect('profile')


@login_required
def notifications(request):
    context = {
        'title': 'Notifications',
        'Notifications': 'active_link',
        'objects': Notification.objects.filter(target=request.user)
    }
    return render(request, 'Auth/notifications.html', context)