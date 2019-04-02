FROM python:3
HEALTHCHECK --interval=8s --timeout=3s --retries=14 \
  CMD curl --fail localhost:5000/ || exit 1
COPY ["webscript.py", "list_pip_pkg.txt", "./"]
RUN pip install --no-cache-dir  -r list_pip_pkg.txt
CMD [ "python", "./webscript.py"]
