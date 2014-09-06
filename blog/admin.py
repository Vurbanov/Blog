from django.contrib import admin
from blog.models import Post, Comments


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'category', 'body_text')
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'email', 'body', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
