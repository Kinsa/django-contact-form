import os

from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

VERSION = 1.6

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
    install_requires=['django>=1.8', 'django-floppyforms'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite="runtests.runtests",
)
