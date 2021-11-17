from django import forms
from django.db.models import fields
from .models import Community_review, Community_comment
from accounts.models import Account

class Community_reviewForm(forms.ModelForm):
    class Meta:
        model = Community_review
        fields = ('title', 'content',)

class Community_commentForm(forms.ModelForm):
    class Meta:
        model = Community_comment
        fields = ('content',)