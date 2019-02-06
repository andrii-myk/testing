from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question',]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }