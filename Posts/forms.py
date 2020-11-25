from django import forms
from .models import Tag, Post, Message


class PostCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField( queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = Post
        fields = ['image', 'caption', 'tags']


class MessageCreateForm(forms.ModelForm):
    OPTIONS = (
		('Report bugs', 'Report bugs'),
		('Report security issues', 'Report security issues'),
		('Help for projects', 'Help for projects'),
		('For business', 'For business'),
		('Others', 'Others'),
	) 


    subject = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)

    
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject','message']