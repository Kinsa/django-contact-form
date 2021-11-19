from smtplib import SMTPRecipientsRefused

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from .forms import ContactForm


def send_mail_wrapped(current_site_name, message, recipients, sent_from):
    send_mail(
        f'Message from {current_site_name}',  # Email Subject
        f'{message}',  # Email Body
        sent_from,  # Email From Value (Sender)
        [i[1] for i in recipients],  # Email Recipients
    )


def contact(request):
    try:
        current_site_name = Site.objects.get_current().name
    except Site.DoesNotExist:
        current_site_name = 'your website'

    recipients = getattr(settings, 'CONTACT_FORM_RECIPIENTS', settings.MANAGERS)

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            sender_email = form.cleaned_data['email']

            message = 'Message from: %s\n---\n\n%s' % (
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )

            send_mail_wrapped(
                current_site_name,
                message,
                recipients,
                settings.DEFAULT_FROM_EMAIL  # don't use `sender_email`, DMARC spoofing filters may kick in and prevent the mail from being sent
            )

            return HttpResponseRedirect(reverse('contact:success'))
    else:
        form = ContactForm()

    if request.is_ajax():
        return render(
            request,
            'contact/form.html',
            {'form': form},
        )
    else:
        return render(
            request,
            'contact/contact_form.html',
            {'form': form},
        )
