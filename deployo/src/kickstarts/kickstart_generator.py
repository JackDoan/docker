from deployo.src.kickstarts.kickstart_file import KickstartFile as ks
import deployo.src.docker.swarm as swarm


class KickstartGenerator:
    # epel_repo = ks.repo_spec("EPEL", "http://dl.fedoraproject.org/pub/epel/7/x86_64/")
    firstboot_script_url = "{{ request.url_root[:-1] + url_for('get_firstboot_script', spec=spec) }}"

    def __init__(self):
        pass

    swarm_script = [swarm.get_join_cmd()]

    specs = {}

    specs['base'] = ks(). \
        timezone("America/Chicago"). \
        rootpw("password"). \
        use_simple_partitions(). \
        repo("Latest", "http://centos.mirror.lstn.net/7/os/x86_64/"). \
        repo("Extras", "http://centos.mirror.lstn.net/7/extras/x86_64/"). \
        repo("Updates", "http://centos.mirror.lstn.net/7/updates/x86_64/"). \
        add_packages(ks.simple_packages)

    specs['docker-host'] = specs['base']. \
        repo("Docker CE Stable - x86_64", "https://download.docker.com/linux/centos/7/x86_64/stable/", True). \
        add_package("docker-ce"). \
        append_header("services --enabled docker")

    specs['swarm-node'] = specs['docker-host']. \
        add_firstboot(firstboot_script_url, swarm_script)

    def get(self, spec):
        if spec in self.specs:
            return self.specs[spec]
        else:
            return "#Warning: " + spec + " was not in the dictionary" + self.specs['base'].__str__()

    def get_firstboot(self, spec):
        to_return = "echo no script defined"
        if spec in self.specs:
            if self.specs[spec].firstboot is not None:
                to_return = self.specs[spec].firstboot

        return to_return
