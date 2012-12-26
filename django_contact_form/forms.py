import re

from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='Your email address')
    message = forms.CharField(widget=forms.Textarea)
    captcha = forms.CharField(label='What is the sum of six and seven?')

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        if not re.search(r"thirteen|13", capcha, re.IGNORECASE):
            raise forms.ValidationError("Double check your math.")
        return captcha

