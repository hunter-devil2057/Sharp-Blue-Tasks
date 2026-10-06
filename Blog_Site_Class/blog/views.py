from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse

from .models import Blog
from .forms import CommentForm, BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        # return HttpResponse("<h1>Hello, this is Home Page....</h1>")
        posts = Blog.objects.all()
        carousel = Blog.objects.all().order_by('-id')
        return render(request, 'home.html', {'posts': posts, 'carousel': carousel})

class BlogList(View):
    def get(self, request):
        posts = Blog.objects.all()      # ORM, one type of encapsulation
        # carousel = Blog.objects.all().order_by('-id')[:4]
        carousel = Blog.objects.all().order_by('-id')
        return render(request, 'list.html', {'posts': posts, 'carousel': carousel})

class BlogDetail(View):
    def get(self, request, pk):
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

class PostLike(View):
    def get(self, request, pk):
        post = get_object_or_404(Blog, pk=pk)
        post.likes += 1
        post.save()
        return redirect('detail', pk=pk)

class Search(View):
    def get(self, request):
        query = request.GET.get('q', '')        # q is the name of the search field's placeholder
        results = Blog.objects.filter(title__icontains=query)        # case insensitive
        # title is the name of the field.
        return render(request, 'search.html', {'query': query, 'results': results})

class CreateBlog(View):
    def get(self, request):
        form = BlogForm(request.POST or None, request.FILES or None)       # received from Forms.py

        if request.method == "POST" and form.is_valid():
            post = form.save()
            return redirect("detail", pk=post.pk)

        return render(request, "blog_form.html", {
            "form": form,
            "page_title": "Add Blog",
        })

class UpdateBlog(View):
    def get(self, request, pk):
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

class DeleteBlog(View):
    def get(self, request, pk):
        post = get_object_or_404(Blog, pk = pk)

        if request.method == "POST":
            post.delete()
            return redirect("list")
        return render(request, "blog_confirm_delete.html", {
            "post": post,
        })
# class AboutView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Hello, this is About Page....</h1>")

# class HelpView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Hello, this is Help View......</h1>")

# class ContactView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Hello, this is Contact View......</h1>")