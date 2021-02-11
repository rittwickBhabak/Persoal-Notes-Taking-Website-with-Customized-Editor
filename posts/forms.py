from django import forms 
from posts.models import Post 
from posts.models import Tag 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
