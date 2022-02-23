from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes', 'tags')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')


admin.site.register(Tag)
