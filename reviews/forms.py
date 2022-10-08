from dataclasses import field
from tkinter import Widget
from django import forms
from django import forms
from django.forms import TextInput
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade', 'img_url']