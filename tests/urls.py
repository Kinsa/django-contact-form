from django.conf.urls import include, url


urlpatterns = [
    url(r'^contact/', include('django_contact_form.urls', namespace='contact')),
]
