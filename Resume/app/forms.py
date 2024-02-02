from django import forms
from .models import ResumeModel
from django.forms import TextInput, EmailInput, Textarea, FileInput

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['name', 'email', 'address', 'phone','education','photo', 'skills','projects']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style':'width:300px'}),
            'email': EmailInput(attrs={'class': 'form-control','style':'width:300px'}),
            'address': Textarea(attrs={'class': 'form-control', 'rows': 3,'style':'width:300px'}),
            'phone': TextInput(attrs={'class': 'form-control', 'rows': 3,'style':'width:300px'}),
            'photo': FileInput(attrs={'class': 'form-control-file','style':'width:300px'}),
            'education': TextInput(attrs={'class': 'form-control','style':'width:300px'}),
            'skills': Textarea(attrs={'class': 'form-control', 'rows': 5,'style':'width:300px'}),
            'projects': TextInput(attrs={'class': 'form-control','style':'width:300px'}),
        }
