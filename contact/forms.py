from django import forms

# to send the contact form entries as an E-mail
class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)