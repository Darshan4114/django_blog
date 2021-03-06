from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta(object):
        model = Blog
        fields = ['blog_title', 'blog_text', 'blog_img']