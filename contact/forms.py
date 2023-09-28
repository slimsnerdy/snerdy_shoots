from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from django.forms.utils import ErrorList, ErrorDict
from django.utils.safestring import mark_safe

class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "first name"}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "last name"}), required=False)
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', "placeholder": "email"}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "subject"}), required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "placeholder": "message"}), required=True)
    instagram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "instagram"}), required=False)
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'form-control', "placeholder": "👈 enter the chars"}), required=True, error_messages={'invalid': 'u are a bot 🤖'})

class DivErrorDict(ErrorDict):
    # def __str__(self):
    #     return self.as_divs()
    # def as_divs(self):
    #     if not self: return ''
    #     return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])

    template_name = 'django/forms/errors/dict/text.txt'

class DivErrorList(ErrorList):
    # def __str__(self):
    #     return self.as_divs()
    # def as_divs(self):
    #     if not self: return ''
    #     return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])
    #     return mark_safe('<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self]))

    template_name = 'django/forms/errors/list/text.txt'