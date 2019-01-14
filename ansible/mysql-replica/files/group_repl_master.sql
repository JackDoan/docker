SET SQL_LOG_BIN=0;
SET GLOBAL group_replication_bootstrap_group=1;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group=0;
SET SQL_LOG_BIN=1;
SELECT * FROM performance_schema.replication_group_members;
