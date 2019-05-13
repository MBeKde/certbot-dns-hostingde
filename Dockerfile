FROM certbot/certbot

COPY . src/certbot-dns-hostingde

RUN pip install --no-cache-dir --editable src/certbot-dns-hostingde
