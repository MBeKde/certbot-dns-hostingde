docker run -it --rm \
        -v letsencrypt:/etc/letsencrypt  \
        -v /docker/web/log/letsencrypt:/var/log/letsencrypt \
        -v /root/hostingde.ini:/hostingde.ini  \
        initit:certbot-hostingde \
        renew \
        -a certbot-dns-hostingde:dns-hostingde  \
        --certbot-dns-hostingde:dns-hostingde-credentials /hostingde.ini \
