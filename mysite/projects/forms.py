from .models import ProjectComment
from django import forms

class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = ProjectComment
        fields = ('project', 'reviewer', 'content',)
        widgets = {'project': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}