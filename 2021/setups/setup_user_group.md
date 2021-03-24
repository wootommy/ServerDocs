# 服务器用户、用户组、权限管理

### 权限管理

-   类 Linux 的系统都具有基本的权限管理。用户分组，组分权限，权限管理区分所有者、归属组、其他。一个文件只能归属于一个用户、组。使用`ls -l`指令查看文件权限。

```sh
$ ls -l .zshrc # -ld for folder
-rwxrwxrwx 1 tommy  staff  2259 Aug 14 12:27 .zshrc
# 10-digits, link times, owner, group, size, last modify time, file name
# digit 0: d,directroy -,regular file s,socket l,symbolic link
# b,block-oriented device file c,charcter-oriented device file
```

-   权限类型分为读、写、执行（r4、w2、x1）。使用`chmod`指令进行管理。支持数字替身。

```sh
chmod [options] [mode] [file]
# [options]: -R/--recursive, dir and files inside
# [mode]: [ugoa][[+-=][rwxX]]
# [mode]: 600,644,666,700,711,755,777

# examples:
chmod a+r,ug+w,o-w a.conf b.xml
chmod -R a+rw * # all files
chmod 777 mine.txt
```

### 用户、用户组管理

-   重装系统之后，第一次建立的账户是管理员账户，需要主动初始化 root 账户。使用管理员或 root 账户去创建其他普通账户。

```sh
sudo passwd root # change passwd for root
[sudo] password for nami-442: # admin passwd
...
```

-   查看一些用户信息与系统文件。

```sh
$ whoami # w
zfj

$ id zfj
uid=1027(zfj) gid=1028(zfj) groups=1028(zfj),0(root),27(sudo)

# files
cat /etc/passwd |grep username # user info
cat /etc/shadow |grep username # passwd info
cat /etc/group |grep groupname # group info

zfj:x:1027:0::/home/zfj:/home/linuxbrew/.linuxbrew/bin/zsh
# user info: name:x:uid:gid:others:login shell path

zfj:*****
# passwd info: name:hashpasswd

anaconda:x:id:hpc,zfj
# group info: name:x:gid:users
```

-   管理用户、用户组。

```sh
# manage
sudo adduser username # add user
sudo userdel -r username # delete user and home dir

sudo addgroup groupname # add group
sudo groupdel groupname # delete group

sudo adduser username groupname # add user to group
sudo gpasswd -d userName groupName # delete user from group

# maintain
passwd [login_user] # change passwd for current user
sudo usermod -g root [login_user] # change group
sudo usermod -s /home/linuxbrew/.linuxbrew/bin/zsh [login_user] # change login shell
```
