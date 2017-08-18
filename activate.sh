#!/bin/bash
#docker run -i -t --rm -v /home/pzzh/project/portia:/app/data/projects:rw -p 9001:9001 scrapinghub/portia
#docker run -i -t --rm -v /home/pzzh/project/portia:/app/data/projects:rw -p 9001:9001 83f1647dd657

basepath=$(cd `dirname $0`; pwd)
echo $basepath
docker run -t --rm -v $basepath/projects:/app/data/projects:rw -v $basepath/slyd:/app/slyd:rw -p 9001:9001 new_portia ./app/docker/entry
