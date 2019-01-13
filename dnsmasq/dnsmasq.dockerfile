FROM alpine:edge
RUN apk --no-cache add dnsmasq
EXPOSE 53 53/udp
COPY dnsmasq.conf /dnsmasq.conf
COPY ./tftp /tftp

ENTRYPOINT ["dnsmasq", "-k", "--log-facility=-"]
