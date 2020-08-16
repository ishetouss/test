from django import forms
from .models import Comment, Reply, Message, Volunteer


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    
    email = forms.EmailField(widget=forms.EmailInput(
    attrs={
        "class": "form-control",
        "placeholder": "Leave your email!"
        })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
    

    class Meta():
        model = Comment
        fields = ['author','email',]
        


class ReplyForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
    

    class Meta():
        model = Comment
        fields = ['author', 'body',]

class MessageForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    
    email = forms.EmailField(widget=forms.EmailInput(
    attrs={
        "class": "form-control",
        "placeholder": "Leave your email!"
        })
    )
    subject = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject"
        })
    )

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a message!"
        })
    )
    

    class Meta():
        model = Message
        fields = ['name','email','subject', 'message',]
        
        

class VolunteerForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your volunteer Name"
        })
    )
    email = forms.EmailField(widget=forms.EmailInput(
    attrs={
        "class": "form-control",
        "placeholder": "Leave your email!"
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

    class Meta():
        model = Volunteer
        fields = ['name','email','message',]
        