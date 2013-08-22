from smtplib import SMTPRecipientsRefused

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django_contact_form.forms import ContactForm


def send_mail_wrapped(cleaned_data, current_site_name, recipients, sender_email):
    send_mail(
        'Message from %s' % current_site_name,  # Email Subject
        cleaned_data['message'],  # Email Body
        sender_email,  # Email From Value (Sender)
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
            cleaned_data = form.cleaned_data
            sender_email = cleaned_data.get('email', cleaned_data['email'])

            try:
                send_mail_wrapped(cleaned_data, current_site_name, recipients, sender_email)
            except SMTPRecipientsRefused:  # Some clients (Google, Microsoft) want you to use their SMTP servers
                send_mail_wrapped(cleaned_data, current_site_name, recipients, settings.DEFAULT_FROM_EMAIL)

            return HttpResponseRedirect(reverse('success'))
    else:
        form = ContactForm()

    if request.is_ajax():
        return render_to_response('contact/form.html', {'form': form},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('contact/contact_form.html', {'form': form},
                                  context_instance=RequestContext(request))
