from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField( 
                widget=forms.Textarea(
                        attrs={'placeholder': "Your message", 
                               "class": "form-control"}))

    class Meta:
        model = Post
        fields = ["text", ]
