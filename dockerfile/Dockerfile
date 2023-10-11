FROM        --platform=$TARGETOS/$TARGETARCH mcr.microsoft.com/playwright/python:v1.38.0-jammy

LABEL       author="Len"

RUN         apt update \
            && apt -y install git gcc g++ ca-certificates dnsutils curl iproute2 ffmpeg procps libnss3 libglib2.0-0 libgconf-2-4 \
            && useradd -m -d /home/container container

RUN         apt -f install -y
RUN         apt-get install -y wget
RUN         wget -q https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.198-1_amd64.deb
RUN         apt-get install ./google-chrome-stable_114.0.5735.198-1_amd64.deb -y


USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        /entrypoint.sh /entrypoint.sh
CMD         [ "/bin/bash", "/entrypoint.sh" ]