FROM alpine:latest
MAINTAINER Konstantin Kuzmenko 'ikkv@yandex.ru'
HEALTHCHECK --interval=8s --timeout=3s --retries=14 \
  CMD curl --fail localhost:5000/ || exit 1
RUN apk update
RUN apk add curl python3
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip setuptools
# RUN set -e; \
# 	apk add --no-cache --virtual .build-deps \
# 		gcc \
# 		libc-dev \
# 		linux-headers \
#     python3-dev \
# 	; \
# 	pip install -r list_pip_pkg.txt; \
# 	apk del .build-deps;
RUN pip3 install -r list_pip_pkg.txt
RUN chmod 755 webscript.py
EXPOSE 5000
ENTRYPOINT ["./webscript.py"]
