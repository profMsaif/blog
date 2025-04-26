from django import forms

from blog_app import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("name", "email", "body")
