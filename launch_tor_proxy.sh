#!/bin/bash

# Set the password environment variable
PASSWORD="${PASSWORD:-randompwd}"

# Remove the existing container if it exists and then run a new container
docker rm -f tor_proxy || true && \
docker run -dit \
    --name tor_proxy --hostname tor_proxy \
    -p 8118:8118 -p 9050:9050 -p 9051:9051 \
    -e PASSWORD="$PASSWORD" \
    dperson/torproxy \
    bash -c "/usr/bin/torproxy.sh -p $PASSWORD"