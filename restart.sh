#!/bin/bash

WORKDIR=/home/$(whoami)/Documents/blog_source/docs

source /home/$(whoami)/miniforge3/bin/activate blog
rm -rf ${WORKDIR}/build

cd ${WORKDIR}
make html

cp ${WORKDIR}/source/BingSiteAuth.xml  ${WORKDIR}/build/html
cp ${WORKDIR}/source/sitemap.xml ${WORKDIR}/build/html
cp ${WORKDIR}/source/robots.txt ${WORKDIR}/build/html
cp -r ${WORKDIR}/source/storage  ${WORKDIR}/build/html
cp -r ${WORKDIR}/source/jieba_tmp  ${WORKDIR}/build/html
