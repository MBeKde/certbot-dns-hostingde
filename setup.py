import sys

from setuptools import setup
from setuptools import find_packages


version = '0.1.0'

install_requires = [
    'acme>=0.21.1',
    'certbot>=0.21.1',
    'setuptools',
    'zope.interface',
]

setup(
    name='certbot-dns-hostingde',
    version=version,
    description="hosting.de DNS Authenticator plugin for Certbot",
    url='https://github.com/initit/certbot-dns-hostingde',
    author='Michael Brueckner',
    author_email='github@initit.de',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-hostingde = certbot_dns_hostingde.dns_hostingde:Authenticator',
        ],
    }
)
