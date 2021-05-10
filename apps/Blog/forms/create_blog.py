from django  import forms
from ..models import Blog

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = '__all__'
        widgets = {'blog_title':forms.TextInput(attrs={'class':'form-control','placeholder':'Blog Title'}),
                  'category':forms.Select(attrs={'class':'form-control','placeholder':'category'}),
                  'language':forms.TextInput(attrs={'class':'form-control','placeholder':'language'}),
                  'blog':forms.Textarea(attrs={'class':'form-control','placeholder':'Blog'}),
                  'author':forms.Select(attrs={'class':'form-control','placeholder':'Author'}),
                  'keyword':forms.TextInput(attrs={'class':'form-control','placeholder':'Keywords','id':"keyword"})
                }