from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_contact_form.forms import ContactForm


def contact(request):
    try:
        current_site_name = Site.objects.get_current().name
    except Site.DoesNotExist:
        current_site_name = 'your website'

    recipients = getattr(settings, 'CONTACT_FORM_RECIPIENTS', settings.MANAGERS)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                'Message from %s' % current_site_name,  # Email Subject
                cd['message'],  # Email Body
                cd.get('email', cd['email']),  # Email From Value (Sender)
                [i[1] for i in recipients],  # Email Recipients
            )
            return HttpResponseRedirect(reverse('success'))
    else:
        form = ContactForm()

    if request.is_ajax():
        return render_to_response('contact/form.html', {'form': form},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('contact/contact_form.html', {'form': form},
                                  context_instance=RequestContext(request))
