FROM php:7.4-apache

RUN apt-get update && apt-get install -y \
    openssh-server \
    rsyslog \
    && mkdir /var/run/sshd \
    && docker-php-ext-install mysqli

RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'root:root' | chpasswd && \
    echo 'LogLevel VERBOSE' >> /etc/ssh/sshd_config && \
    echo 'SyslogFacility AUTH' >> /etc/ssh/sshd_config && \
    echo 'UsePAM yes' >> /etc/ssh/sshd_config

RUN rm -f /var/log/apache2/access.log && \
    rm -f /var/log/apache2/error.log && \
    sed -i 's|CustomLog /dev/stdout|CustomLog /var/log/apache2/access.log|' /etc/apache2/apache2.conf && \
    sed -i 's|ErrorLog /dev/stderr|ErrorLog /var/log/apache2/error.log|' /etc/apache2/apache2.conf

RUN touch /var/log/apache2/access.log && chmod 666 /var/log/apache2/access.log
RUN touch /var/log/apache2/error.log && chmod 666 /var/log/apache2/error.log
RUN touch /var/log/auth.log && chmod 666 /var/log/auth.log

COPY . /var/www/html/

RUN echo 'auth,authpriv.* /var/log/auth.log' >> /etc/rsyslog.conf && \
    echo 'daemon.* /var/log/syslog' >> /etc/rsyslog.conf

EXPOSE 80 22

CMD service rsyslog start && service ssh start && apache2-foreground
