from django.shortcuts import render, redirect
from blog.forms import CommentForm
from blog.models import Post, Comments
from django.db.models import Q


def home_page(request):
    posts = Post.objects.all().order_by("-pub_date")[:1]
    return render(request, "blog/index.html", {'posts': posts,
                                               'user': request.user})


def post(request, post_id):
    if request.method == "POST":
        p = request.POST
        author = "Anonymous"
        if p["author"]:
            author = p["author"]
        comment = Comments(post=Post.objects.get(pk=post_id))
        comment_form = CommentForm(request.POST, instance=comment)
        comment_form.fields["author"].required = False
        comment = comment_form.save(commit=False)
        comment.author = author
        comment.save()
        return redirect('blog/posts.html', args=(post_id,))
    post = Post.objects.get(pk=post_id)
    comments = Comments.objects.filter(post=post)
    context = {'post': post, 'user': request.user, 'comments': comments,
               'form': CommentForm()}
    return render(request, 'blog/posts.html', context)


def publications(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/publications.html', {'posts': posts,
                                                      'user': request.user})


def contacts(request):
    return render(request, 'blog/contacts.html', {'user': request.user})


def search(request):
    searched_string = request.POST.get('searched_post', "")
    posts = Post.objects.filter(
        Q(title__icontains=searched_string) | Q(category__icontains=searched_string))\
        .order_by('-pub_date')
    return render(request, 'blog/results.html', {'posts': posts,
                                                 'user': request.user})
