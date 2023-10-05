FROM        --platform=$TARGETOS/$TARGETARCH python:3.11-slim

LABEL       author="Michael Parker" maintainer="parker@pterodactyl.io"

RUN         apt update \
            && apt -y install git gcc g++ ca-certificates dnsutils curl iproute2 ffmpeg procps libnss3 libglib2.0-0 libgconf-2-4 \
            && useradd -m -d /home/container container

RUN         apt-get install -y wget
RUN         wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
            && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN         apt-get update && apt-get -y install google-chrome-stable

USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        /entrypoint.sh /entrypoint.sh
CMD         [ "/bin/bash", "/entrypoint.sh" ]