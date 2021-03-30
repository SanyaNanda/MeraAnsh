from django import forms
from .models import Post, Prescriptions

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'reciever','body','file')
		

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
			'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'sanya', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Details'}),
			# 'file': forms.FileField()
		}

class PresForm(forms.ModelForm):
	class Meta:
		model = Prescriptions
		fields = ('title', 'author', 'reciever','body')
		

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
			'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'sanya', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Prescriptions'}),
			# 'file': forms.FileField()
		}