from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    # create form
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    # create model form for comment model
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
