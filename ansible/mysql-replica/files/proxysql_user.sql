
SET sql_log_bin=0;
CREATE USER 'proxysql'@'%' IDENTIFIED BY 'ProxySQLPa55';
GRANT USAGE ON *.* TO 'proxysql'@'%';
SET sql_log_bin=1;
