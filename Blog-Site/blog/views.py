from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import CommentForm, BlogForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog_list(request):
    posts = Blog.objects.all()      # ORM, one type of encapsulation
    # carousel = Blog.objects.all().order_by('-id')[:4]
    carousel = Blog.objects.all().order_by('-id')
    return render(request, 'list.html', {'posts': posts, 'carousel': carousel})

def blog_detail(request, pk):       # pk = primary key, should have a unique primary key
    posts = get_object_or_404(Blog, pk=pk)
    print(posts, ": ", posts.__str__())
    comments = posts.comments.all()
    form = CommentForm()
    if request.method == "POST":
        if request.POST.get('action') == 'like':
            posts.likes += 1
            posts.save(update_fields=['likes'])
            return redirect('detail', pk=pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = posts
            comment.save()
            return redirect('detail', pk=pk)
    return render(request, 'detail.html', {'posts': posts, 'form': form, 'comments': comments})


def post_like(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.likes += 1
    post.save()
    return redirect('detail', pk=pk)


def search(request):
    query = request.GET.get('q', '')        # q is the name of the search field's placeholder
    results = Blog.objects.filter(title__icontains=query)        # case insensitive
    # title is the name of the field.
    return render(request, 'search.html', {'query': query, 'results': results})

# Performing CRUD Operation
# Creating a Blog Post
def blog_create(request):
    form = BlogForm(request.POST or None, request.FILES or None)       # received from Forms.py

    if request.method == "POST" and form.is_valid():
        post = form.save()
        return redirect("detail", pk=post.pk)

    return render(request, "blog_form.html", {
        "form": form,
        "page_title": "Add Blog",
    })

# Updating the Created Blog
def blog_update(request, pk):
    # Post khojeko whether it's available or not, 
    # Vetye return garni, else 404 return garni 
    # HTTP Request Code: 404 = details not found
    post = get_object_or_404(Blog, pk=pk) # post = object stored
    print(post, " *************** ")
    print(type(post))
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)     # 
        if form.is_valid():     # valid vaneko data check garxa, pathayeko thik xaki xaina vanera
            post = form.save()
            return redirect("detail", pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, "blog_form.html", {
        "form": form, 
        "page_title": "Update Blog", 
        "post": post,
    })

def blog_delete(request, pk):
    post = get_object_or_404(Blog, pk = pk)

    if request.method == "POST":
        post.delete()
        return redirect("list")
    return render(request, "blog_confirm_delete.html", {
        "post": post,
    })