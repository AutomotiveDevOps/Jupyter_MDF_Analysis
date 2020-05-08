#!/usr/bin/env bash
export SCRIPT=`realpath $0`
echo ${SCRIPT}
export DIR=`dirname ${SCRIPT}`
echo ${DIR}

docker build --file Dockerfile-alternate --tag jupyter_mdf_analysis:dev .
docker run --workdir /home/jovian --interactive --tty --volume ${DIR}:/home/jovian jupyter_mdf_analysis_jupyter make docs
