import os

from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__),
              'README.rst')).read()

VERSION = __import__('django_contact_form').__version__

setup(
    name='django-contact-form',
    version=VERSION,
    description="Contact Form for Django",
    long_description=README,
    author='Joe Bergantine',
    author_email='jbergantine@gmail.com',
    maintainer='Joe Bergantine',
    maintainer_email='jbergantine@gmail.com',
    url='https://github.com/jbergantine/django-contact-form',
    license='New BSD License',
    install_requires=['django>=1.4', 'django-floppyforms'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
