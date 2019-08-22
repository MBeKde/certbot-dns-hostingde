"""Tests for certbot_dns_gehirn.dns_gehirn."""

import unittest

import mock
from requests.exceptions import HTTPError

from certbot.compat import os
from certbot.plugins import dns_test_common
from certbot.plugins import dns_test_common_lexicon
from certbot.plugins.dns_test_common import DOMAIN
from certbot.tests import util as test_util

AUTH_TOKEN = 'MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw'


class AuthenticatorTest(
    test_util.TempDirTestCase,
    dns_test_common_lexicon.BaseHostingdeAuthenticatorTest):

    def setUp(self):
        super(AuthenticatorTest, self).setUp()

        from certbot_dns_hostingde.dns_hostingde import Authenticator

        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write(
            {"hostingde_auth_token": AUTH_TOKEN, },
            path
        )

        self.config = mock.MagicMock(hostingde_credentials=path,
                                     hostingde_propagation_seconds=0)  # don't wait during tests

        self.auth = Authenticator(self.config, "hostingde")

        self.mock_client = mock.MagicMock()
        # _get_gehirn_client | pylint: disable=protected-access
        self.auth._get_hostingde_client = mock.MagicMock(return_value=self.mock_client)


class HostingdeLexiconClientTest(unittest.TestCase, dns_test_common_lexicon.BaseHostingdeClientTest):
    DOMAIN_NOT_FOUND = HTTPError('404 Client Error: Not Found for url: {0}.'.format(DOMAIN))
    LOGIN_ERROR = HTTPError('401 Client Error: Unauthorized for url: {0}.'.format(DOMAIN))

    def setUp(self):
        from certbot_dns_hostingde.dns_hostingde import _HostingdeLexiconClient

        self.client = _HostingdeLexiconClient(AUTH_TOKEN, 0)

        self.provider_mock = mock.MagicMock()
        self.client.provider = self.provider_mock


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
