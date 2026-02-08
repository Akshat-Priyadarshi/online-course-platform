from django import forms
from .models import Course, OnlineContent

class AddContentForm(forms.ModelForm):
    # Dropdown to select the course the instructor wants to add content to
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), 
        label="Select Course",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = OnlineContent
        fields = ['title', 'content_type', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Lecture 1: Intro to SQL'}),
            'content_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., PDF, Video, Link'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/material'}),
        }