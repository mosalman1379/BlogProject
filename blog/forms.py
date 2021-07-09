from django import forms


class EmailPostForm(forms.Form):
    # create form
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False,widget=forms.Textarea)
