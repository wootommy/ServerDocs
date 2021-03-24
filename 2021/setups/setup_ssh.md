# Linux 配置 SSH 远程登录

配置 SSH 远程连接。

### SSH、openssh

-   SSH 为 Secure Shell 的缩写，由 IETF 的网络小组制定，为建立在应用层基础上的安全协议，专为远程登录会话和其他网络服务提供安全性的协议。
-   OpenSSH 是 SSH 协议的免费开源实现，提供了服务端后台程序和客户端工具，用来加密远程控制和文件传输过程中的数据，并由此来代替原来的类似服务。

### 配置 openssh

-   查看网络配置，主要查看 IP 地址。

```sh
# install network tools if not installed
sudo apt-get install net-tools
ifconfig

en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	...
	inet 192.168.1.101 netmask 0xffffff00 broadcast 192.168.1.255
	...
```

-   安装相应的客户端。进行配置。

```sh
# server and client
sudo apt install openssh-server openssh-client

# register and start service
systemctl enable ssh
systemctl start ssh
service ssh start
/etc/init.d/ssh start
```

-   还有很多的高级配置呀！例如限制 session 并发数量，限制端口，提升账户验证方式等。

```sh
# config file: /etc/ssh/sshd_config

Protocol 2,1 # ssh version 1 and 2
Host * # all IPs server
ListenAddress 0.0.0.0 # all IPs
Port 22 # default port
PasswordAuthentication yes # passwd
PermitEmptyPasswords no # no empty passwd
CheckHostIP yes # check DNS
LoginGraceTime 60 # passwd input time limit

Compression yes # compress commands
SyslogFacility AUTH # log
LogLevel INFO # log level
PermitRootLogin no # no root login
```

### 防火墙设置

-   最好是有一个防火墙的配置，推荐使用 firewalld。

```sh
# firewalld
sudo apt install firewalld

# manage ports
sudo firewall-cmd --permanent --add-port=22/tcp
sudo firewall-cmd --permanent --add-service=ssh

# check config
sudo firewall-cmd --list-all
```

### 刷新 DNS 与 IP

```sh
# hosts
sudo gedit /etc/hosts

# refresh
sudo /etc/init.d/dns-clean start
sudo /etc/init.d/networking restart
```

### 远程登录

-   内网或使用 VPN 才可以进入。

```sh
ssh username@100.64.212.206
```
