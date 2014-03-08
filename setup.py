import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

version = __import__('django_contact_form').__version__

setup(
    name='django-contact-form',
    version=version,
    description="Contact Form for Django",
    long_description="""django-contact-form creates a contact form application
for Django projects. See the project page for more information:
  https://github.com/jbergantine/django-contact""",
    author='Joe Bergantine',
    author_email='jbergantine@gmail.com',
    maintainer='Joe Bergantine',
    maintainer_email='jbergantine@gmail.com',
    url='https://github.com/jbergantine/django-contact-form',
    license='New BSD License',
    install_requires=['django-floppyforms'],
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
