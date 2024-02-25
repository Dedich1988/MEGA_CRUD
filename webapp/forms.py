from django import forms

class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 5:
            raise forms.ValidationError("Сообщение должно содержать не менее 5 символов.")
        return message
