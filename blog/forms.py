from django import forms
from tinymce.widgets import TinyMCE
from django.core import validators
from blog.models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))
    title = forms.CharField(validators=[validators.MinLengthValidator(3, message="En az 3 karakterden oluşmalı!.")])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]
