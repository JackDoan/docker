FROM alpine:edge
RUN apk --no-cache add dnsmasq
EXPOSE 53 53/udp
ADD dnsmasq.conf /etc/dnsmasq.conf
ENTRYPOINT ["dnsmasq", "-k", "--log-facility=-"]
