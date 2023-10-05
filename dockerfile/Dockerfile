FROM        --platform=$TARGETOS/$TARGETARCH python:3.11-slim

LABEL       author="Michael Parker" maintainer="parker@pterodactyl.io"

RUN         apt update \
            && apt -y install git gcc g++ ca-certificates dnsutils curl iproute2 ffmpeg procps libnss3 libglib2.0-0 libgconf-2-4 \
            && useradd -m -d /home/container container

RUN         apt -f install -y
RUN         apt-get install -y wget
RUN         wget -q https://dl.google.com/linux/direct/google-chrome-stable_114_md64.deb
RUN         apt-get install ./google-chrome-stable_current_amd64.deb -y

USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        /entrypoint.sh /entrypoint.sh
CMD         [ "/bin/bash", "/entrypoint.sh" ]