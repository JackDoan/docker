FROM alpine:edge
RUN apk --no-cache add dnsmasq
EXPOSE 53 53/udp
COPY ./tftp /tftp

ENTRYPOINT ["dnsmasq", "-k", "--log-facility=-"]
