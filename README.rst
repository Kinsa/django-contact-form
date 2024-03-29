=====================
 Django Contact Form
=====================

A contact form application for Django.

Installation from Source
========================

::

 $ git clone git@github.com:Kinsa/django-contact-form.git
 $ cd django-contact-form
 $ python setup.py install

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following lines:

::

 -e git://github.com/Kinsa/django-contact-form.git@master#egg=django_contact_form

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

Setup the Project For the Application
=====================================

Add to the project's ``settings.py`` file tuple of installed apps: ::

 'django_contact_form',

In the project's ``urls.py`` file add: ::

 url(r'^contact/',
     include('django_contact_form.urls', namespace='contact')),

This makes the form available at ``{% url 'contact:contact' %}`` and the success page available at ``{% url 'contact:success' %}``.

Setup the Recipients of the Contact Form
========================================

Form submissions will go to either a list of recipients defined in a custom tuple called ``CONTACT_FORM_RECIPIENTS`` or, if that can't be found in the settings file, the list of ``MANAGERS``. The format for ``CONTACT_FORM_RECIPIENTS`` should follow the format for ``MANAGERS`` and should look something like: ::

 CONTACT_FORM_RECIPIENTS = (
     ('Barack Obama', 'barack@whitehouse.gov'),
 )

Configure Email Settings for Sending
====================================

In the project's ``settings.py`` file, add and configure the following: ::

 EMAIL_HOST = ''
 EMAIL_HOST_USER = ''
 EMAIL_HOST_PASSWORD = ''
 DEFAULT_FROM_EMAIL = ''
 SERVER_EMAIL = DEFAULT_FROM_EMAIL

Configure the Templates
=======================

By default the templates contain only the bare necessities. To override the default templates, create a directory called contact in your templates directory and add 2 files: ``contact_form.html`` and ``thanks.html``. If you're using virtualenv, to copy the templates from the project in order to make adjustments to them, ``cd`` to the root of the django project and execute the following command: ::

 cp -r $VIRTUAL_ENV/src/django-contact-form/django_contact_form/templates/contact templates/contact

Enable the Sites Framework if Desired
=====================================

With the Sites Framework enabled, the subject of the contact form will indicate that it is from the name of the currently enabled website. Without this the subject indicates the form has been sent by 'your website'.

To enable the Sites Framework, `follow the directions in the Django documentation <https://docs.djangoproject.com/en/dev/ref/contrib/sites/#enabling-the-sites-framework>`_.

Developing
==========

django_contact_form follows the `Git Flow branching model <http://nvie.com/posts/a-successful-git-branching-model/>`_.

When releasing, bump the version number in the project's ``setup.py`` file.

Testing
-------

::

 $ python setup.py test

With TOX
^^^^^^^^

First, install Tox, then run the tests. This will test against the Django versions specified in the environments specified in the ``tox.ini`` file

::

 $ pip install tox
 $ tox
