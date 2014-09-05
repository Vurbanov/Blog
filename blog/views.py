from django.shortcuts import render, redirect
from blog.forms import CommentForm
from blog.models import Post, Comments


def home_page(request):
    posts = Post.objects.all().order_by("-pub_date")[:1]
    return render(request, "blog/index.html", {'posts': posts, 'user': request.user})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comments.objects.filter(post=post)
    context = {'post': post, 'user': request.user, 'comments': comments, 'form': CommentForm()}
    return render(request, 'blog/posts.html', context)

def add_comment(request, pk):
    p = request.POST
    if 'body' in p and p["body"]:
        author = "Anonymous"
        if p["author"]:
            author = p["author"]
        comment = Comments(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False
        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return redirect('posts.html', args=[pk])

def publications(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/publications.html', {'posts': posts, 'user': request.user})

def contacts(request):
    return render(request, 'blog/contacts.html', {'user': request.user})

