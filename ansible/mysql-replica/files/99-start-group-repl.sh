#!/bin/bash
#!/bin/bash

echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "                          TEST                                  "
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo 'group_replication_start_on_boot = ON' > /etc/my.cnf.d/99-start-group-repl.conf
ls /etc
ls /etc/my.cnf*

#sed -i 's/group_replication_start_on_boot = OFF/group_replication_start_on_boot = ON/g' /etc/my.cnf
