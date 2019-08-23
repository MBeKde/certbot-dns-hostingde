FROM certbot/certbot

RUN pip install --no-cache-dir dns-lexicon
RUN pip install https://github.com/initit/certbot-dns-hostingde/archive/master.zip
COPY ./lexicon /usr/local/lib/python2.7/site-packages/lexicon/providers/
