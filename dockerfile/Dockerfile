FROM		--platform=$TARGETOS/$TARGETARCH ghcr.io/parkervcp/yolks:python_3.11

LABEL		author="JewishLewish" maintainer="lenny@lunes.host"

LABEL		org.opencontainers.image.source="https://github.com/matthewpi/images"
LABEL		org.opencontainers.image.licenses=MIT

RUN         apt update \
            && apt -y install libglib2.0-0=2.50.3-2 libnss3=2:3.26.2-1.1+deb9u1 libgconf-2-4=3.2.6-4+b1 libfontconfig1=2.11.0-6.7+b1