from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #форма для заполнения поста
    class Meta:
        #определяем, какая модель будет использоваться для создания формы
        model = Post
        fields = ('title', 'text',)