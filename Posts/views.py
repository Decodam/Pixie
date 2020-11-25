from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostCreateForm, MessageCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .filters import *
from Auth.models import *
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('feeds')
    else:
        return render(request, 'index.html')

def about(request):
    if request.user.is_authenticated:
        return redirect('feeds')
    else:
        if request.method == "POST":
            form = MessageCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Successfully posted your message!!!')

        else:
            form = MessageCreateForm()

        return render(request, 'about.html', {"form": form})


@login_required
def feeds(request):
    context = {
        'title': 'feeds',
        'posts': Post.objects.all(),
        'Home': 'active_link'
    }
    return render(request, 'App/feeds.html', context)


@login_required
def add_comment_to_post(request, pk):
    if request.method == 'POST':
        comment_input = request.POST['comment']
        user = request.user

        comment = Comment.objects.create(author=user, content=comment_input)
        comment.save

        post = get_object_or_404(Post, pk=pk)
        post_update = post.comments.add(comment)
    

    return redirect('scream_details', pk=pk)


@login_required
def scream_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = post.author
    context = {
        'title': 'scream details',
        'target_post': post,
        'posts': Post.objects.filter(author=user),
        'Home': 'active_link'
    }
    return render(request, 'App/details.html', context)


@login_required
def add_like_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('scream_details', pk=pk)


@login_required
def add_heart_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.hearts.all():
        post.hearts.remove(request.user)
    else:
        post.hearts.add(request.user)

    return redirect('scream_details', pk=pk)


@login_required
def create_new_scream(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        form.instance.author = request.user

        if form.is_valid():
            form.save()

            message = f'Check it out!!! {request.user} has a new scream for you!'
            new_post = get_object_or_404(Post, pk=form.instance.id)

            for user in request.user.profile.followers.all():

                username = user.username
                email = user.email
                
                subject, from_email, to = f'{request.user.username} posted a new scream!', 'pixie.social.official@gmail.com', email
                
                text_content = f"Hey {username}, Your friend {request.user.username} have just posted a new scream!!! you can check it out by clicking this link! Thanking you, Pixie"
                
                html_content = f"<p>hey <strong>{username}</strong>,</p> <p>Your friend {request.user.username} have just posted a new scream!!! you can check it out by clicking this <a href='http://127.0.0.1:8000/scream/details/{form.instance.id}/' >link!</a></p> <p>Thanking you,<br>Pixie</p>"
                
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()


                create_notification = Notification.objects.create(user=request.user, content=message, target=user, post=new_post)
                create_notification.save()

            messages.success(request, f'Successfully created your scream!!!')
            return redirect('scream_details', pk=form.instance.id)

    else:
        form = PostCreateForm()

    context = {
        'title': 'New Scream',
        'Scream': 'active_link',
        'form': form
    }
    
    return render(request, 'App/add_scream.html', context)




@login_required
def update_existing_scream(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.author:
        if request.method == 'POST':

            form = PostCreateForm(request.POST, request.FILES, instance=post)
            form.instance.author = request.user

            if form.is_valid():
                form.save()

                message = f'Check it out!!! {request.user} has a update his old post!'
                new_post = get_object_or_404(Post, pk=form.instance.id)

                for user in request.user.profile.followers.all():

                    username = user.username
                    email = user.email

                    subject, from_email, to = f'{request.user.username} updated his scream!', 'pixie.social.official@gmail.com', email

                    text_content = f"Hey {username}, Your friend {request.user.username} have just updated one of his old screams!!! you can check it out by clicking this link! Thanking you, Pixie"

                    html_content = f"<p>hey <strong>{username}</strong>,</p> <p>Your friend {request.user.username} have just updated one of his old screams!!! you can check it out by clicking this <a href='http://127.0.0.1:8000/scream/details/{form.instance.id}/' >link!</a></p> <p>Thanking you,<br>Pixie</p>"

                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()



                    create_notification = Notification.objects.create(user=request.user, content=message, target=user, post=new_post)
                    create_notification.save()

                messages.success(request, f'Successfully update your post!!!')
                return redirect('scream_details', pk=form.instance.id)

        else:
            form = PostCreateForm(instance=post)
    else:
        return redirect('scream_details', pk=post.id)

    

    context = {
        'title': 'New Scream',
        'Scream': 'active_link',
        'form': form
    }
    
    return render(request, 'App/update_scream.html', context)


@login_required
def delete_existing_scream(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.author:
        post.delete()
        messages.success(request, f'Successfully deleted your post!!!')
        return redirect('feeds')
    else:
        return redirect('scream_details', pk=post.id)

@login_required
def add_scream_to_Bookmarks(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post in request.user.profile.bookmarks.all():
        request.user.profile.bookmarks.remove(post)

    else:
        request.user.profile.bookmarks.add(post)

    return redirect('scream_details', pk=pk)

@login_required
def report_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    message = f'{request.user.username} had reported {post} please check it out on this url -> http://127.0.0.1:8000/scream/details/{post.id}/'


    create_message = Message.objects.create(name=request.user.username, email=request.user.email, subject="Report posts", message="message")
    create_message.save()
    messages.success(request, f'Successfully reported about this scream!!!')
    
    return redirect('scream_details', pk=pk)

'''
    Explore Page Views Over Here!!!
'''
@login_required
def explore(request):
    if request.method == 'POST':
        tag_input = request.POST['tag_name']
        tag_name = tag_input.replace("#", "")

        tag_count = Tag.objects.filter(name=tag_name).count()

        if tag_count != 0:
            message = f'Sorry {request.user.username}, that tag already exists!'
            messages.warning(request, message)
        else:
            new_tag = Tag.objects.create(name=tag_name)
            new_tag.save()
            message = f'Hey {request.user.username}, successfully created your tag!'
            messages.success(request, message)

    context = {
        'title': 'Explore',
        'users': User.objects.all().order_by('?')[:15],
        'posts': Post.objects.all().order_by('?')[:25],
        'Explore': 'active_link'
    }
    return render(request, 'App/explore.html', context)


@login_required
def tag_filter(request, pk):
    context = {
        'title': 'scream tags',
        'target_tag': get_object_or_404(Tag, pk=pk),
        'posts': Post.objects.all(),
        'Explore': 'active_link'
    }
    return render(request, 'App/tags_explore.html', context)


@login_required
def search_users(request):
    users= Profile.objects.all().order_by('-followers')
    Filter = Userfilter(request.GET, queryset=users)
    users = Filter.qs 

    context = {
        'search_filter': Filter,
        'search_users': users,
        'title': "Search Tags",
        'Search': 'active_link'
    }

    return render(request, 'App/search_users.html', context)


@login_required
def search_tags(request):
    tags= Tag.objects.all()
    Filter = Tagfilter(request.GET, queryset=tags)
    tags = Filter.qs 

    context = {
        'search_filter': Filter,
        'search_users': tags,
        'title': "Search Tags",
        'Search': 'active_link'
    }

    return render(request, 'App/search_tags.html', context)