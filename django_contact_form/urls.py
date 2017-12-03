from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import contact

app_name = 'contact'

urlpatterns = [
    url(r'^$', contact, {}, 'contact'),
    url(
        r'^thanks/$',
        TemplateView.as_view(template_name='contact/success.html'),
        name='success'
    ),
]
