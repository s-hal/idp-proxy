#!/bin/bash
working_dir="/home/stefanh/docker/proxy-idp"
cmd="/usr/local/bin/docker-compose"
start_dir=`pwd`

cd ${working_dir}
${cmd} -f docker-compose-build.yaml run --rm py-builder 
cd ${start_dir}
