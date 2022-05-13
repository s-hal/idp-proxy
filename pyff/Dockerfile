# run.docker
FROM py-base

RUN apt-get update 

ADD wheelhouse /wheelhouse

RUN . /appenv/bin/activate && \
    pip3 install --no-index -f /wheelhouse pyFF

COPY pyff/config/pyff/ /opt/pyff

CMD . /appenv/bin/activate && \
      pyffd -f -H 0.0.0.0 --loglevel=DEBUG --frequency=120 -P 8081 -p /tmp/pyffd.pid /opt/pyff/mdx.fd 
