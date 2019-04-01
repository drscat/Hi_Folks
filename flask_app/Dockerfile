FROM alpine:latest
HEALTHCHECK --interval=8s --timeout=3s --retries=14 \
  CMD curl --fail localhost:5000/ || exit 1
COPY ["webscript.py", "list_pip_pkg.txt", "./"]
RUN apk add --no-cache curl python3; \
  pip3 install --no-cache-dir  --upgrade pip setuptools; \
  pip3 install --no-cache-dir  -r list_pip_pkg.txt
CMD [ "python3", "./webscript.py"]
