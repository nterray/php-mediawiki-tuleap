FROM alpine:3.8

RUN apk --no-cache add git php7 php7-iconv php7-tokenizer php7-xmlwriter php7-simplexml php7-phar && \
    apk add --virtual .build-dependencies --no-cache ca-certificates openssl && \
    wget https://github.com/squizlabs/PHP_CodeSniffer/releases/download/3.3.1/phpcs.phar -O /usr/local/bin/phpcs && \
    chmod +x /usr/local/bin/phpcs && \
    wget https://github.com/wimg/PHPCompatibility/archive/8.2.0.tar.gz -O /tmp/8.2.0.tar.gz && \
    mkdir /app && cd /app && tar -xf /tmp/8.2.0.tar.gz && \
    mv PHPCompatibility-8.2.0 PHPCompatibility && \
    phpcs --config-set installed_paths /app/PHPCompatibility && \
    apk del .build-dependencies && rm /tmp/8.2.0.tar.gz
