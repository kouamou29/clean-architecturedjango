from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, label='Title',
    widget=forms.TextInput(attrs={'placeholder': 'Enter post title', 'class': 'py-2 px-2 w-full border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    content = forms.CharField( required=True, label='Content', widget=forms.Textarea(attrs={'placeholder':'Write your post content here', 
                                                                                                                 'class': 'py-2 px-2 w-full  border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    class Meta:
        model = Post
        fields = ['title', 'content', 'category'] 
        
        widgets = {
            'category': forms.Select(attrs={'class': 'py-2 px-2 w-full border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
    