from django import forms
from blog.models import Post

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'Captions']