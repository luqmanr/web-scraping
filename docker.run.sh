#!/bin/bash
docker run --rm -it \
--network=host \
-v `pwd`:`pwd` \
-w `pwd` \
webscraper:2.0 \
bash
