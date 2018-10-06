FROM nginx:mainline-alpine
COPY arch-install /usr/share/nginx/html/archiso/arch-install
COPY centos-kick /usr/share/nginx/html/centos-kick