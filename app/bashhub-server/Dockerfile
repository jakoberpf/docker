FROM alpine:3.18

ENV BASHHUB_VERSION v0.2.5

RUN apk update && apk add --no-cache ca-certificates libc6-compat libstdc++ wget

RUN ARCH=$(arch | sed s/aarch64/arm64/ | sed s/x86_64/amd64/) ; \
    wget https://github.com/nicksherron/bashhub-server/releases/download/${BASHHUB_VERSION}/bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}.tar.gz && \
    tar -zxvf bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}.tar.gz && \
    mv bashhub-server_${BASHHUB_VERSION}_linux_${ARCH}/bashhub-server /usr/bin/
RUN chmod +x /usr/bin/bashhub-server

VOLUME /data
WORKDIR /data

EXPOSE 8080

ENTRYPOINT ["bashhub-server"]
CMD [ "--db", "./data.db"]
