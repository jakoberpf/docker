FROM alpine:3.11

ENV BASHHUB_VERSION v0.2.5

RUN apk update && apk add --no-cache ca-certificates libc6-compat libstdc++ curl

RUN ARCH=$(arch | sed s/aarch64/arm64/ | sed s/x86_64/amd64/) ; \
    curl https://github.com/nicksherron/bashhub-server/releases/download/${BASHHUB_VERSION}/bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}.tar.gz -o bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}.tar.gz && \
    tar xz bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}.tar.gz --directory . && \
    rm bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}.tar.gz && \
    mv bashhub-server /usr/bin/bashhub-server

VOLUME /data
WORKDIR /data

EXPOSE 8080

ENTRYPOINT ["bashhub-server"]
CMD [ "--db", "./data.db"]
