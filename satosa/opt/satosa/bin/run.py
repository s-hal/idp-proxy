#!/usr/bin/python3
import subprocess
import shlex
import sys
import re

msg_prefix = "SATOSA: FILTER: "
log_filters = (('received attributes', 'received attributes'),
               ('SAML response', '\'SAMLResponse\': \''),
               ('SAML2 attribute converter', 'SATOSA: [saml2.attribute_converter]'))
def run_command(command):
    buffering = False
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        line = process.stdout.readline().decode(sys.stdout.encoding).strip()
        if line == '' and process.poll() is not None:
            break
        if line:
            if line.startswith("SATOSA:") and line.endswith("_EnD_"):
                buffering = False
                output = line[:-5]
            elif line.startswith("SATOSA:"):
                buffering = True
                output = line
            elif line.endswith("_EnD_"):
                buffering = False
                output = output + "\n" + line[:-5]
            elif buffering:
                output = output + "\n" + line
            else:
               continue
            if not buffering:
                for log_filter in log_filters:
                    #if re.search(log_filter[1], output):
                    if log_filter[1] in output:
                        output = msg_prefix + log_filter[0]
                print(output)
                output = ""
    rc = process.poll()
    return rc

run_command("gunicorn -b0.0.0.0:443 satosa.wsgi:app --keyfile=/opt/satosa/pki/gunicorn.key --certfile=/opt/satosa/pki/gunicorn.crt")
