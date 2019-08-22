"""DNS Authenticator for Hosting.de Infrastracture Service DNS."""
import logging

import zope.interface
from lexicon.providers import hostingde

from certbot import interfaces
from certbot.plugins import dns_common
from certbot.plugins import dns_common_lexicon

logger = logging.getLogger(__name__)

DASHBOARD_URL = "https://www.hosting.de/"


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for Hosting.de Infrastracture Service DNS

    This Authenticator uses the Hosting.de Infrastracture Service API
    to fulfill a dns-01 challenge.
    """

    description = 'Obtain certificates using a DNS TXT record (if' + \
                  ' you are using Hosting.de Infrastracture Service for DNS).'
    ttl = 60

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(
            Authenticator, cls).add_parser_arguments(
                add, default_propagation_seconds=30)
        add(
            'credentials',
            help='Hosting.de Infrastracture Service credentials file.')

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return 'This plugin configures a DNS TXT record to respond to a ' + \
               'dns-01 challenge using the Hosting.de ' + \
                'Infrastracture Service API.'

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'Hosting.de Infrastracture Service credentials file',
            {
                'auth-token': 'Auth Token for Hosting.de Infrastructure '
                              'Service API obtained from {0}'.format(
                                  DASHBOARD_URL),
            }
        )

    def _perform(self, domain, validation_name, validation):
        self._get_hostingde_client().add_txt_record(
            domain, validation_name, validation)

    def _cleanup(self, domain, validation_name, validation):
        self._get_hostingde_client().del_txt_record(
            domain, validation_name, validation)

    def _get_hostingde_client(self):
        return _HostingdeLexiconClient(
            self.credentials.conf('auth-token'),
            self.ttl
        )


class _HostingdeLexiconClient(dns_common_lexicon.LexiconClient):
    """
    Encapsulates all communication with the Hosting.de Infrastracture Service
    via Lexicon.
    """

    def __init__(self, auth_token, ttl):
        super(_HostingdeLexiconClient, self).__init__()

        config = dns_common_lexicon.build_lexicon_config('hostingde', {
            'ttl': ttl,
        }, {
            'auth_token': auth_token,
        })

        self.provider = hostingde.Provider(config)
