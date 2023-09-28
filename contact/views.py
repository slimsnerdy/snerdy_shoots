# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, DivErrorList

from django.contrib import messages #import messages

from environs import Env

env = Env()
env.read_env()

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        # form = ContactForm(request.POST, error_class=DivErrorList)
        # form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body =  {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'from_email': form.cleaned_data['from_email'],
                'message': form.cleaned_data['message'],
                'instagram': form.cleaned_data['instagram'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, env.str('DB_EMAIL'), [env.str('DB_EMAIL')])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'THANK YOU message received')
            return redirect('home')
        # messages.error(request, 'Error. Message not sent.')
        # messages.error(request, form.errors)

    # form = ContactForm()
    return render(request, 'contact.html', {'form': form})