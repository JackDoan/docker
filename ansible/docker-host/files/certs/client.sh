
mkdir -p client
cd client
rm ./*.pem
openssl genrsa -out key.pem 2048
openssl req -new -key key.pem -out cert.csr \
    -subj '/CN=docker-client'
openssl x509 -req -in cert.csr -CA ../ca.pem \
    -CAkey ../ca-key.pem -CAcreateserial \
    -out cert.pem -days 3650 -extensions v3_req
cp ../ca.pem .
rm ./*.csr

