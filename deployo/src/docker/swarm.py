import subprocess

join_token_cmd = ["docker", "swarm", "join-token", "-q", "worker"]
manager_ip_cmd = ["docker", "node", "inspect", "self", "--format", "{{ .ManagerStatus.Addr }}"]


def get_join_cmd():
    return "\necho Joining the swarm...\n" \
           "docker swarm join --token " + \
           subprocess.check_output(join_token_cmd).decode("utf-8") + " " + \
           subprocess.check_output(manager_ip_cmd).decode("utf-8") + "\n"
