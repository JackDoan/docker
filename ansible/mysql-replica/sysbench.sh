#!/usr/bin/env bash

#mysql -u root -ppassword -h manager1 -P 6033 < prep.sql

docker run \
--rm=true \
severalnines/sysbench \
sysbench \
--db-driver=mysql \
--report-interval=2 \
--mysql-table-engine=innodb \
--oltp-table-size=100000 \
--oltp-tables-count=24 \
--threads=64 \
--time=99999 \
--mysql-host=10.1.0.80 \
--mysql-port=3306 \
--mysql-user=root \
--mysql-password=password \
/usr/share/sysbench/tests/include/oltp_legacy/oltp.lua \
run
