from django.contrib import admin

from .models import Post, Rubric


class PostAdmin(admin.ModelAdmin):
 list_display = ('rubric','title', 'content', 'price', 'published')
 list_display_links = ('title', 'content')
 search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Rubric)
