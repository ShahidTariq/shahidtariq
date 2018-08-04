from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    fname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True,)