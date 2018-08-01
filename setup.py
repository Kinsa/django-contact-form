import os

from setuptools import setup, find_packages

description = "Contact Form for Django"
long_description = description

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='django-contact-form',
    version='1.6.2',
    packages=find_packages(exclude=["tests"]),
    install_requires=['django>=1.11', 'django-floppyforms'],
    author='Joe Bergantine',
    author_email='joe.bergantine@gmail.com',
    description=description,
    long_description=long_description,
    url='https://github.com/jbergantine/django-contact-form',
    download_url='https://github.com/jbergantine/django-contact-form/tarball/1.6.1',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
)
