from django import forms
from .models import Publication, Commentaire

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['content']
