from django.test import TestCase
from django.test.client import Client

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class RoutingTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_dict = {'email': 'nobody@example.com',
                          'message': 'This is a test message.',
                          'captcha': '13'}

    def test_form_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('contact:contact'))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'contact/contact_form.html')

        # Issue a POST request.
        response = self.client.post(reverse('contact:contact'),
                                    self.post_dict,
                                    follow=False)

        # Check that the response is 302 Redirect (theoretically to the success page).
        self.failUnlessEqual(response.status_code, 302)

    def test_thanks_url(self):
        response = self.client.post(reverse('contact:contact'),
                                    self.post_dict,
                                    follow=True)

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'contact/success.html')

        # Check that the response is being properly routed.
        self.assertRedirects(
            response,
            reverse('contact:success'),
        )

    def test_message_is_required(self):
        self.post_dict['message'] = ''
        response = self.client.post(reverse('contact:contact'),
                                    self.post_dict)
        self.assertFormError(response, 'form', 'message',
                             [u'This field is required.'])

    def test_email_address_is_required(self):
        self.post_dict['email'] = ''
        response = self.client.post(reverse('contact:contact'),
                                    self.post_dict)
        self.assertFormError(response, 'form', 'email',
                             [u'This field is required.'])

    def test_email_adderss_is_valid(self):
        self.post_dict['email'] = 'nobody@example'
        response = self.client.post(reverse('contact:contact'), self.post_dict)
        self.assertFormError(response, 'form', 'email',
                             [u'Enter a valid email address.'])

    def test_captcha_accepts_integer(self):
        response = self.client.post(reverse('contact:contact'),
                                    self.post_dict,
                                    follow=True)

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'contact/success.html')

        # Check that the response is being properly routed.
        self.assertRedirects(
            response,
            reverse('contact:success'),
        )

    def test_captcha_does_not_accept_string(self):
        self.post_dict['captcha'] = 'thirteen'

        response = self.client.post(reverse('contact:contact'),
                                    self.post_dict,
                                    follow=True)
        self.assertFormError(response, 'form', 'captcha',
                             [u'Enter a whole number.'])

    def test_captcha_fails_with_invalid_value(self):
        self.post_dict['captcha'] = 78
        response = self.client.post(reverse('contact:contact'), self.post_dict)
        self.assertFormError(response, 'form', 'captcha',
                             [u'Double check your math.'])

    def test_captcha_is_required(self):
        self.post_dict['captcha'] = ''
        response = self.client.post(reverse('contact:contact'), self.post_dict)
        self.assertFormError(response, 'form', 'captcha',
                             [u'This field is required.'])
