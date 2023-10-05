FROM        --platform=$TARGETOS/$TARGETARCH python:3.11-slim

LABEL       author="Michael Parker" maintainer="parker@pterodactyl.io"

RUN         apt update \
            && apt -y install git gcc g++ ca-certificates dnsutils curl iproute2 ffmpeg procps libnss3 libglib2.0-0 libgconf-2-4 \
            && useradd -m -d /home/container container

RUN         CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
            mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
            curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
            unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
            rm /tmp/chromedriver_linux64.zip && \
            chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
            ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver


RUN         apt -f install -y
RUN         apt-get install -y wget
RUN         wget -q https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.198-1_amd64.deb
RUN         apt-get install ./google-chrome-stable_114.0.5735.198-1_amd64.deb -y


USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        /entrypoint.sh /entrypoint.sh
CMD         [ "/bin/bash", "/entrypoint.sh" ]