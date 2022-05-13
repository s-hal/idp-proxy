FROM py-base

RUN apt-get update && \
    apt-get install -y xmlsec1 python3-gdbm libffi-dev libssl-dev

ADD wheelhouse /wheelhouse

COPY satosa/opt/satosa /opt/satosa

RUN python3 -m venv /appenv && \
    . /appenv/bin/activate && \
    pip3 install --no-index -f /wheelhouse SATOSA

ENV SATOSA_CONFIG=/opt/satosa/proxy_conf.yaml

EXPOSE 8443

CMD . /appenv/bin/activate && \
      gunicorn -b0.0.0.0:8443 satosa.wsgi:app --keyfile=/opt/satosa/pki/gunicorn.key --certfile=/opt/satosa/pki/gunicorn.crt
