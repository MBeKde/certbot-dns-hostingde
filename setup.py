from setuptools import setup
from setuptools import find_packages


version = '0.38.0.dev0'

# Please update tox.ini when modifying dependency version requirements
install_requires = [
    'acme>=0.31.0',
    'certbot>=0.34.0',
    'dns-lexicon>=2.1.22',
    'mock',
    'setuptools',
    'zope.interface',
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-hostingde',
    version=version,
    description="Hosting.de Infrastracture Service DNS Authenticator "
                "plugin for Certbot",
    url='https://github.com/certbot/certbot',
    author="Michael Brückner",
    author_email='mbr@initit.de',
    license='Apache License 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
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
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-hostingde = certbot_dns_hostingde.dns_hostingde:Authenticator'
        ],
    },
    test_suite='certbot_dns_hostingde',
)
