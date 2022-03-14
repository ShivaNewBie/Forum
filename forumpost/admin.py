from django.contrib import admin

# Register your models here.
from .models import ForumPost



class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on','author')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(ForumPost,ForumAdmin)
