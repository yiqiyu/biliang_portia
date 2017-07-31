#!/bin/bash 
docker run -i -t --rm -v /home/pzzh/project/portia:/app/data/projects:rw -p 9001:9001 scrapinghub/portia
