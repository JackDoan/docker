SET SQL_LOG_BIN=0;
CREATE USER rpl_user@'%' IDENTIFIED BY 'R3plic4tion!';
GRANT REPLICATION SLAVE ON *.* TO rpl_user@'%';
FLUSH PRIVILEGES;

CHANGE MASTER TO MASTER_USER='rpl_user', MASTER_PASSWORD='R3plic4tion!' FOR CHANNEL 'group_replication_recovery';

SET SQL_LOG_BIN=1;
