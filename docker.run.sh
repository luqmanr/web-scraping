#!/bin/bash
docker run --rm -it \
-v `pwd`:`pwd` \
-w `pwd` \
webscraper:2.0 \
bash
