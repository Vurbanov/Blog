from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body_text = models.TextField()
    author = models.CharField(max_length=100, default='Vankata')
    category = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)
    email = models.EmailField()