# 关于 Linux 进程命令行管理

想用服务器跑代码自然免不了多进程管理。

### CPU、GPU 性能管理

```sh
# CPU
htop

# GPU
nvidia-smi
```

### 抓取进程号

```sh
ps [-A] [|grep zsh]
pstree
pgrep pname
```

### 控制优先级

```sh
renice level pid
```

### 管理进程

```sh
kill pid
pkill pname
killall pname
```
