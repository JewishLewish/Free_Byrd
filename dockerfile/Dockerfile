#
# Copyright (c) 2023 Matthew Penner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#Similiar to PY 3.11 dockerfile but installs chromium

FROM		--platform=$TARGETOS/$TARGETARCH docker.io/library/python:3.11-alpine

LABEL		author="JewishLewish" maintainer="lenny@lunes.host"

LABEL		org.opencontainers.image.source="https://github.com/matthewpi/images"
LABEL		org.opencontainers.image.licenses=MIT

RUN			apk add --update --no-cache ca-certificates curl ffmpeg g++ gcc git iproute2 openssl sqlite tar tzdata \
				&& adduser -D -h /home/container container

# install google chrome
RUN         wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN         sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN         apt-get -y update
RUN         apt-get install -y google-chrome-stable

# install chromedriver
RUN         apt-get install -yqq unzip
RUN         wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN         unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

USER		container
ENV			USER=container HOME=/home/container
WORKDIR		/home/container

COPY		./entrypoint.sh /entrypoint.sh
CMD			[ "/bin/ash", "/entrypoint.sh" ]