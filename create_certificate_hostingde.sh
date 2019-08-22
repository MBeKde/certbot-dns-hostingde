docker run -it --rm \
        -v letsencrypt:/etc/letsencrypt  \
        -v /docker/web/log/letsencrypt:/var/log/letsencrypt \
        -v /root/hostingde.ini:/hostingde.ini  \
        initit:certbot-hostingde \
        certonly \
        -a certbot-dns-hostingde:dns-hostingde  \
        --certbot-dns-hostingde:dns-hostingde-credentials /hostingde.ini \
        --agree-tos \
        --no-eff-email \
        --email "admin@initit.de" \
        --rsa-key-size 4096 \
        --dns-hostingde-propagation-seconds 10
         -d "eruza.de" -d "*.eruza.de" 