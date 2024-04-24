from django import forms
from .models import Profile, UserNote, UserPost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView





class RegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'id': 'exampleInputUsername'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'exampleInputEmail1'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'exampleInputPassword1'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'exampleInputPassword2'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(LoginView):

    #username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'id': 'exampleInputUsername'}))
    #email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'exampleInputEmail1'}))
    #password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'exampleInputPassword1'}))
   # password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'exampleInputPassword2'}))
    class Meta:
        model = User
        fields = ['username', 'password1']


class ProfileForm(forms.ModelForm):

     #image = forms.ImageField(widget=forms.FileField(attrs={'class': 'form-control'}))
    # address1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     #city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ## state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     #country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    #user = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = Profile
        fields = ['image', 'banner_image', 'header_description', 'address1', 'city', 'zipcode', 'state', 'country', 'username']


class AddNoteForm(forms.ModelForm):
    note_header = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    note_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = UserNote
        fields = ['user','note_header', 'note_details']


class AddPostForm(forms.ModelForm):
    #user = forms.CharField(widget=forms.HiddenInput())
   # post_likes = forms.IntegerField(widget=forms.HiddenInput())
    #post_dislikes = forms.IntegerField(widget=forms.HiddenInput())
    post_header = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    post_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    #post_likes = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    #post_dislikes = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = UserPost
        fields = ['post_header', 'post_details']
