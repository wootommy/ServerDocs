# Linux 配置 conda

### 下载安装文件

-   官网[下载](https://www.anaconda.com/products/individual)。`.sh`文件。
-   切换到 root 账户执行安装。

```sh
# wget
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

# sudo install
su root
bash Anaconda3-2020.07-Linux-x86_64.sh

Anaconda3 will now be installed into this location:
/root/anaconda3
  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below
[/root/anaconda3] >>> /opt/anaconda # normal user will not be able to read /root

conda init
conda avtivate
channels
install with conda
conda create -n env_name
conda update -n env_name
sudo vim /etc/resolv.conf
sudo /etc/init.d/dns-clean start
```
