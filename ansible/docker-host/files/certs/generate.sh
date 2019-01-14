do_cert () {
    SERVER="$1"
    IP="$2"

    openssl genrsa -out "$SERVER"-key.pem 4096

    openssl req -subj '/CN="$SERVER".foxglen.jackdoan.com' \
    -sha256 -new -key "$SERVER"-key.pem \
    -out "$SERVER".csr

    echo "subjectAltName = IP:$IP,IP:127.0.0.1" > $SERVER.extfile

    openssl x509 -req -days 3650 -sha256 -in \
    "$SERVER".csr \
    -CA ca.pem \
    -CAkey ca-key.pem \
    -CAcreateserial \
    -out "$SERVER".pem \
    -extfile $SERVER.extfile
}


rm -f ./*.extfile ./*.pem ./*.csr

openssl genrsa -out ca-key.pem 4096
openssl req -new -x509 -days 3650 -key ca-key.pem -sha256 -out ca.pem -subj '/C=US/ST=Texas/L=Dallas/O=JackDoan/CN=foxglen.jackdoan.com'

do_cert "manager1" "10.1.0.80"
do_cert "node1" "10.1.0.81"
do_cert "node2" "10.1.0.82"

rm -f ./*.csr ./*.extfile