from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, View, CreateView
from .forms import CommentForm, MessageForm, VolunteerForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist




def user_post(request):
    all_items = List.objects.filter(user=request.user)
    return render(request, 'list.html', {'all_items': all_items})

    # paginate_by = 3
 
# def list(request):

    # if request.method == 'POST':
    #     user=request.user
    #     form = ListForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         all_items = List.objects.all()
    #         messages.success(request, 'item has been added to List')
    #         return render(request, 'list.html', {'all_items': all_items})
    # else:
    #     user = request.user
        # all_items = List.objects.filter(user=request.user).order_by('-created_on')
        # return render(request, "list.html", {'all_items':all_items})


def homepage(request):
    blogs = BlogPost.objects.all()
    events = Event.objects.all()
    causes = OurCause.objects.all()
    context = {
        'blogs': blogs,
        'events': events,
        'causes': causes
    }  
    return render(request, 'index.html', context)
    

# class HomeView(ListView):
#     model = BlogPost
#     paginate_by = 3
#     template_name = 'index.html' 
#     def get_queryset(self):
#         queryset = BlogPost.objects.all()
#         return queryset


def detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    categories = Category.objects.all()
    form = CommentForm()
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = Comment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             post=post
    #         )
    #         comment.save()
    # comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {
        "post": post,
        # "comments": comments,
        # "form": form,
        "categories": categories
        
    }
    return render(request, "detail.html", context)

def create_comment(request, post_slug=None):
    if request.method == "POST":
        post = BlogPost.objects.get(slug=post_slug)
        comment = post.comments.create(
            author= request.POST.get('author'),
            email = request.POST.get('email'),
            website = request.POST.get('website'),
            content = request.POST.get('content')
            
        )
        messages.success(request, f"{comment.author} your Comment Submitted")
        return redirect('detail', slug=post_slug)
    else:
        return redirect('detail', slug=post_slug)
    

def about(request):
    return render(request, 'about.html')

def causes(request):
    causes = OurCause.objects.all()
    if request.method == 'POST':
        name= request.POST.get("name")
        email= request.POST.get("email")
        nationality =  request.POST.get("nationality")
        id_number =  request.POST.get("id_number")
        gender =  request.POST.get("gender")
        Volunteer(name=name, email=email, nationality=nationality, id_number=id_number).save()

    context = {
        'causes': causes,
    }
    return render(request, 'causes.html', context)

def blog_index(request):
    posts = BlogPost.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)

class BlogListView(ListView):
    model = BlogPost
    paginate_by = 6
    template_name = 'blog.html'


def gallery(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            message = Volunteer(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"]
            )
            message.save()
    context = {
        "form": form, 
    }
    return render(request, 'gallery.html', context)

class EventListView(ListView):
    model = Event
    paginate_by = 3
    template_name = 'event.html' 


def contact(request):
    if request.method == "POST":
        message = Message(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message')
        )
        message.save()
        messages.success(request, f"Message sent")
        return redirect('contact')
    else:
        return render(request, 'contact.html')

def create_comment(request, post_slug=None):
    if request.method == "POST":
        post = BlogPost.objects.get(slug=post_slug)
        comment = post.comments.create(
            author= request.POST.get('author'),
            email = request.POST.get('email'),
            website = request.POST.get('website'),
            content = request.POST.get('content')    
        )
        messages.success(request, f"{comment.author} your Comment Submitted")
        return redirect('detail', slug=post_slug)
    else:
        return redirect('detail', slug=post_slug)

def volunteer(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            message = Volunteer(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"]
            )
            message.save()
    context = {
        "form": form, 
    }
    return render(request, "volunteer.html", context)




def cause_detail(request, slug):
    post = OurCause.objects.get(slug=slug)
    categories = Category.objects.all()
    # form = OurCauseCommentForm()
    # if request.method == 'POST':
    #     form = OurCauseCommentForm(request.POST)
    #     if form.is_valid():
    #         comment = OurCauseComment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             cause=cause
    #         )
    #         comment.save()
    # comments = Comment.objects.filter(cause=cause).order_by('-created_on')
    context = {
        "post": post,
        # "comments": comments,
        # "form": form,
        "categories": categories
        
    }
    return render(request, "cause-detail.html", context)


def blog_category(request, category):
    children = BlogPost.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )
    context = {
        "category": category,
        "children": children
    }
    return render(request, 'blog_category.html', context)

def filter_abana(request, category):
    programs = Program.objects.filter(
        categories__name__contains=category
    )
    
    context = {
        "category": category,
        "programs": programs
    }
    return render(request, 'filter_program.html', context)




def program(request):
    abana = Program.objects.all()
    categories = WorkCategory.objects.all()
    context = {
        'abana': abana,
        'categories': categories,
    }
    return render(request, 'program.html', context)

def program_detail(request, slug):
    program = Program.objects.get(slug=slug)
    recents = Program.objects.all()
 
    context = {
        "program": program,
        'recents': recents
    }
    return render(request, 'program_detail.html', context)

