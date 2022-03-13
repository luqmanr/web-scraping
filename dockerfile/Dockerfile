# prodfrbase is used to install large dependencies for prodfr.
FROM python:3.8.9

# download selenium
RUN python -m pip install --user -U pip
RUN python -m pip install --user --default-timeout=100 \
    selenium==4.1.2 \
    opencv-python==4.5.5.64 \
    numpy==1.22.3 \
    tqdm==4.63.0

# download google-chrome and chromedriver
RUN wget \
    https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    https://chromedriver.storage.googleapis.com/98.0.4758.102/chromedriver_linux64.zip

# install google-chrome
RUN apt-get update && apt-get install -y \
    ./google-chrome-stable_current_amd64.deb \
    --fix-broken

# extract chromedriver
RUN python -m zipfile -e chromedriver_linux64.zip \
    /usr/bin/