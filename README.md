# certbot-dns-hostingde
certbot dns plugin for hosting.de

This plugin automates the process of completing a ``dns-01`` challenge by creating, and subsequently removing, TXT records using the (JSON-based) hosting.de API.
As of the time written ( August 2019) the pull request for the lexicon provider for hosting.de is not approved.
Therefor you have to manual copy the lexicon provider (see `dockerfile`)

Credentials
-----------
Use of this plugin requires a configuration file containing hosting.de API key, obtained from your hosting.de account's [hosting.de Konto / Benutzer / Übersicht -> Details anzeigen](https://secure.hosting.de/account/users/overview). Create an API Key with at least `Dynamic DNS / Hostname` and `Dynamic DNS / Zugänge` full permission.

```ini
# hosting.de API Key used by Certbot
certbot_dns_hostingde:dns_hostingde_auth_token =  +9L$rHdwAAq34$sFmDdvfg54LoznAiJXDwj%+M7TmXZmWc+rJ
```

The path to this file can be provided interactively or using the `--certbot_dns_hostingde:dns-hostingde-credentials` command-line argument. Certbot records the path to this file for use during renewal, but does not store the file's contents.

> You should protect these API credentials as you would the password to your hosting.de account. Users who can read this file can use these credentials to issue arbitrary API calls on your behalf. Users who can cause Certbot to run using these credentials can complete a ``dns-01`` challenge to acquire new certificates or revoke existing certificates for associated domains, even if those domains aren't being managed by this server. Certbot will emit a warning if it detects that the credentials file can be accessed by other users on your system. The warning reads "Unsafe permissions on credentials configuration file", followed by the path to the credentials file. This warning will be emitted each time Certbot uses the credentials file, including for renewal, and cannot be silenced except by addressing the issue (e.g., by using a command like `chmod 600` to restrict access to the file).

# Usage

## Docker

* **Recommended usage**. Create the credentials file and 2 folders for the certificates and logs and run:
```sh
docker run -it --rm \
  -v $(pwd)/certs:/etc/letsencrypt \
  -v $(pwd)/logs:/var/log/letsencrypt \
  -v $(pwd)/hostingde.ini:/hostingde.ini \
  initit/certbot-dns-hostingde certonly \
  -a certbot-dns-hostingde:dns-hostingde \
  --certbot-dns-hostingde:dns-hostingde-credentials /hostingde.ini \
  --agree-tos \
  --email "your@mail.com" \
  -d "example.com" \
  --test-cert
```
* After a successful run, remove the last parameter `--test-cert` which enabled [staging server](https://letsencrypt.org/docs/staging-environment/) and run again.

## Python

* If you know what you're doing install the plugin into the same python environment like `certbot`. In any other case follow the `Docker` approach above:
```sh
pip install https://github.com/initit/certbot-dns-hostingde/archive/master.zip
```
* Check that `certbot` discovers the plugin:
```sh
certbot plugins
```
* Now run the command:
```sh
certbot certonly \
  -a certbot-dns-hostingde:dns-hostingde \
  --certbot-dns-hostingde:dns-hostingde-credentials ~/.secret/certbot/hostingde.ini \
  --agree-tos \
  --email "your@mail.com" \
  -d "example.com" \
  --test-cert
  ```
