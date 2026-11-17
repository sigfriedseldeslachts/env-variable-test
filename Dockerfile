FROM busybox:stable
COPY index.cgi /www/cgi-bin/index.cgi
RUN chmod +x /www/cgi-bin/index.cgi
CMD date +%s > /tmp/start && exec httpd -f -p 80 -h /www
