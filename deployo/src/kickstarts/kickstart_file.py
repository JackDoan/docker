# taken from:
# https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/sect-kickstart-syntax

import crypt


class KickstartFile:
    eula_agree = "eula --agreed"
    auth = "auth --enableshadow --passalgo=sha512"
    use_text_mode = "text"
    no_first_boot_agent = "firstboot --disable"
    us_locale = ["keyboard us", "lang en_US.UTF-8"]
    no_firewall = "firewall --disabled"
    install_log_level = "logging --level=info"
    no_x11 = "skipx"
    no_selinux = "selinux --disabled"
    reboot_when_done = "reboot"
    ignore_unsupported_hw = "unsupported_hardware"
    package_tag = "%packages"
    package_tag_light = package_tag + " --nocore"
    pre_tag = "%pre --log=/var/log/kickstart_pre.log"
    post_tag = "%post --log=/var/log/kickstart_post.log"
    end_tag = "%end"

    simple_partitions = ["zerombr",
                         "bootloader --location=mbr --driveorder=sda --append=\"console=ttyS0,115200 console=tty0\""
                         "clearpart --all --initlabel",
                         "autopart --type=lvm --fstype=xfs --nohome"
                         ]

    simple_header = [eula_agree, auth, use_text_mode, no_firewall, us_locale,
                     no_firewall, install_log_level, no_x11, no_selinux,

                     ignore_unsupported_hw,
                     reboot_when_done
                     ]

    core_packages = [
        "audit                  ",
        "basesystem             ",
        "bash                   ",
        "btrfs-progs            ",
        "coreutils              ",
        "cronie                 ",
        "curl                   ",
        "dhclient               ",
        "e2fsprogs              ",
        "filesystem             ",
        "firewalld              ",
        "glibc                  ",
        "hostname               ",
        "initscripts            ",
        "iproute                ",
        "iprutils               ",
        "iptables               ",
        "iputils                ",
        "irqbalance             ",
        "kbd                    ",
        "kexec-tools            ",
        "less                   ",
        "man-db                 ",
        "ncurses                ",
        "openssh-clients        ",
        "openssh-server         ",
        "parted                 ",
        "passwd                 ",
        "plymouth               ",
        "policycoreutils        ",
        "procps-ng              ",
        "rootfiles              ",
        "rpm                    ",
        "rsyslog                ",
        "selinux-policy-targeted",
        "setup                  ",
        "shadow-utils           ",
        "sudo                   ",
        "systemd                ",
        "tar                    ",
        "tuned                  ",
        "util-linux             ",
        "vim-minimal            ",
        "xfsprogs               ",
        "yum                    ",
        "NetworkManager         ",
        "NetworkManager-team    ",
        "NetworkManager-tui     ",
        "alsa-firmware          ",
        "biosdevname            ",
        "dracut-config-rescue   ",
        "kernel-tools           ",
        "libsysfs               ",
        "linux-firmware         ",
        "microcode_ctl          ",
        "postfix                ",
        "sg3_utils              ",
        "sg3_utils-libs         ",
        "dracut-network         ",
        "initial-setup          ",
        "openssh-keycat         ",
        "rdma-core              ",
        "selinux-policy-mls     ",
        "tboot                  ",
    ]

    wifi_firmware_packages = [
        "aic94xx-firmware       ",
        "ivtv-firmware          ",
        "iwl100-firmware        ",
        "iwl1000-firmware       ",
        "iwl105-firmware        ",
        "iwl135-firmware        ",
        "iwl2000-firmware       ",
        "iwl2030-firmware       ",
        "iwl3160-firmware       ",
        "iwl3945-firmware       ",
        "iwl4965-firmware       ",
        "iwl5000-firmware       ",
        "iwl5150-firmware       ",
        "iwl6000-firmware       ",
        "iwl6000g2a-firmware    ",
        "iwl6000g2b-firmware    ",
        "iwl6050-firmware       ",
        "iwl7260-firmware       ",
        "iwl7265-firmware       ",
    ]

    simple_packages = ["device-mapper-multipath",
                       "rsync", "screen", "tmux",
                       "bash-completion"
                       "usbutils", "net-tools",
                       "vim", "git", "wget"]

    @staticmethod
    def install_spec(url):
        return ["install", "url --url " + url + " --noverifyssl"]

    def install(self, url):
        return self.append_header(self.install_spec(url))

    @staticmethod
    def repo_spec(name, url, install=False):
        repo = "repo --name=\"" + name + "\" " + "--baseurl=" + url
        if bool(install):
            repo += " --install"
        return repo

    def repo(self, name, url, install=False):
        return self.append_header(self.repo_spec(name, url, install))

    @staticmethod
    def timezone_spec(timezone):
        return "timezone --utc " + timezone

    def timezone(self, tz):
        return self.append_header(self.timezone_spec(tz))

    @staticmethod
    def root_password_spec(password):
        return "rootpw --iscrypted " + crypt.crypt(password)

    def rootpw(self, password):
        return self.append_header(self.root_password_spec(password))

    # takes a list or string in, returns it as a flat string nicely line-broken
    # rejects non-strings?
    @staticmethod
    def ks_string(list_in):
        string_out = ""
        if isinstance(list_in, str):
            string_out = list_in + "\n"
        else:
            for i in list_in:
                string_out += KickstartFile.ks_string(i)
        return string_out

    @staticmethod
    def generate_package_spec(pkg_list):
        package_string = "\n" + KickstartFile.package_tag + "\n"
        for pkg in pkg_list:
            package_string += KickstartFile.ks_string(pkg)
        package_string += KickstartFile.end_tag + "\n"
        return package_string

    def __init__(self):
        self.header = self.simple_header
        self.packages = self.core_packages
        self.post = None
        self.pre = None
        self.firstboot = False

    def append_header(self, line):
        self.header += [line]
        return self

    def use_simple_partitions(self):
        self.header.append(self.simple_partitions)
        return self

    def add_package(self, pkg):
        self.packages.append(pkg)
        return self

    def add_packages(self, pkgs):
        self.packages += pkgs
        return self

    def add_firstboot(self, url, contents, name="/root/firstboot.sh"):
        remove_self_from_crontab = "\n\nsed -i '$" + name + "$d' /etc/crontab"
        self.firstboot = self.ks_string([contents, remove_self_from_crontab])
        self.post = [
            "echo \"@reboot root /bin/bash " + name + "\" >> /etc/crontab",
            "curl -o " + name + " " + url,
        ]
        return self

    def __str__(self):
        out = self.ks_string(self.header)
        out += self.generate_package_spec(self.packages)
        if self.pre is not None:
            out += self.pre_tag + "\n" + self.ks_string(self.pre) + "\n" + self.end_tag + "\n"
        if self.post is not None:
            out += self.post_tag + "\n" + self.ks_string(self.post) + "\n" + self.end_tag + "\n"
        return out
