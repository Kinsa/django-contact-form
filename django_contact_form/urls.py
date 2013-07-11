from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from django_contact_form.views import contact


urlpatterns = patterns('',
    url(r'^$', contact, {}, 'contact'),
    url(r'^thanks/$',
        TemplateView.as_view(template_name="contact/success.html"),
        name='success'),
)
