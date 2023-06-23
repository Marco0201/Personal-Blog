from django import forms
from .models import Post, Category

# choices is a query of all the category objects that were made, they need to called by 'name' twice for some reason. It just works
choices = Category.objects.all().values_list('name', 'name')
# print(choices)

# now for this I need to make an empty list because as it is, choices is a query of objects. I need them to be called so i append them to a empty list. Making them into an array I can use for later. You can see what they look like when you print them out.
choice_list = []

for item in choices:
    choice_list.append(item)

# print(choice_list)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'snippet', 'header_image')

        widgets = {
            # the class is technically form-group but this works too, you can find it on the add_post.html file
            # make sure the widgets names match up to the Post models names
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category',
                  'body', 'snippet')

        widgets = {
            # the class is technically form-group but this works too, you can find it on the add_post.html file, and this form will exclude the author field
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
