ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG NMAP_DOWNLOAD_URL

# Content
WORKDIR /nmap

# Install dependencies
RUN apk add --update --no-cache \
            ca-certificates \
            libpcap \
            libgcc \ 
            libstdc++ \
            libretls \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/*

# Compile and install Nmap from sources
RUN apk add --update nmap

ENTRYPOINT ["/usr/bin/nmap"]
