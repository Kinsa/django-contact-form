from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Your email address',
    )

    message = forms.CharField(
        widget=forms.Textarea
    )

    captcha = forms.IntegerField(
        label='What is the sum of six and seven?',
    )

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        if captcha != 13:
            raise forms.ValidationError("Double check your math.")
        return captcha
