FROM certbot/certbot

RUN pip install --no-cache-dir dns-lexicon

COPY . src/certbot-dns-hostingde
COPY ./lexicon /usr/local/lib/python2.7/site-packages/lexicon/providers/
RUN pip install --no-cache-dir --editable src/certbot-dns-hostingde
