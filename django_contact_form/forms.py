from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(label='Your email address')
    message = forms.CharField(widget=forms.Textarea)
    captcha = forms.CharField(label='What is the sum of six and seven?')

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        if not re.search(r"thirteen|13", capcha, re.IGNORECASE):
            raise forms.ValidationError("Double check your math.")
        return captcha

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("This must be at least 4 words in"\
                                        " length.")
        return message
