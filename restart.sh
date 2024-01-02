#!/bin/bash

WORKDIR=/home/junsircoding/Documents/blog_source/docs
# 查询并终止 main.py 的进程
PID=$(ps aux | grep "python -m http.server" | grep -v grep | awk '{print $2}')
echo $PID
if [ -n "$PID" ]; then
    echo "停止进程: $PID"
    kill -9 $PID
else
    echo "服务未运行"
fi

source /home/junsircoding/miniconda3/bin/activate blog
rm -rf ${WORKDIR}/build

cd ${WORKDIR}
make html

cp ${WORKDIR}/source/BingSiteAuth.xml  ${WORKDIR}/build/html
cp ${WORKDIR}/source/google79cba44476b50244.html  ${WORKDIR}/build/html
cp ${WORKDIR}/source/sitemap.xml ${WORKDIR}/build/html
cp -r ${WORKDIR}/source/storage  ${WORKDIR}/build/html

cd ${WORKDIR}/build/html
nohup python -m http.server 2>&1 &
