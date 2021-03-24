# 指令查看系统信息

可以在终端查看服务器的硬件信息，支持本地与远程终端连接。

```note:: 部分储存系统信息的文件仅支持 root 用户查看。

```

## 查询硬件指令汇总

-   查看主板信息。

    ```sh
    > dmidecode -q -t 2
    Base Board Information
        Manufacturer: Gigabyte Technology Co., Ltd.
        Product Name: X299-WU8-CF
        Version: x.x
        Serial Number: Default string
        ...
    ```

-   查看 CPU 信息。

    ```sh
    > dmidecode -q -t 4
    Processor Information
        Socket Designation: <BAD INDEX>
        Type: Central Processor
        Family: Xeon
        Manufacturer: <BAD INDEX>
        ...
    ```

    ```sh
    > cat /proc/cpuinfo |grep "model name" |uniq
    model name	: Intel(R) Core(TM) i9-9980XE CPU @ 3.00GHz
    > cat /proc/cpuinfo |grep "processor" |uniq |wc -l
    36
    ```

-   查看 GPU 信息。

    ```
    > lspci |grep -i nvidia
    19:00.0 VGA compatible controller: NVIDIA Corporation Device 1e04 (rev a1)
    19:00.1 Audio device: NVIDIA Corporation Device 10f7 (rev a1)
    19:00.2 USB controller: NVIDIA Corporation Device 1ad6 (rev a1)
    19:00.3 Serial bus controller [0c80]: NVIDIA Corporation Device 1ad7 (rev a1)
    ...
    ```

    ```sh
    > nvidia-smi
    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 450.57       Driver Version: 450.57       CUDA Version: 11.0     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |                               |                      |               MIG M. |
    |===============================+======================+======================|
    |   0  GeForce RTX 208...  Off  | 00000000:19:00.0 Off |                  N/A |
    | 40%   71C    P2   158W / 250W |   8879MiB / 11019MiB |     54%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+
    |   1  GeForce RTX 208...  Off  | 00000000:1A:00.0 Off |                  N/A |
    | 47%   83C    P2   121W / 250W |   8879MiB / 11019MiB |     54%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+
    |   2  GeForce RTX 208...  Off  | 00000000:67:00.0 Off |                  N/A |
    | 36%   61C    P2    69W / 250W |   6081MiB / 11019MiB |      4%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+
    |   3  GeForce RTX 208...  Off  | 00000000:68:00.0  On |                  N/A |
    | 44%   82C    P2   181W / 250W |   9450MiB / 11018MiB |     55%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+
    ```

-   查看内存信息。

    ```sh
    > dmidecode -q -t 17
    Memory Device
        Array Handle: 0x003D
        Error Information Handle: Not Provided
        Total Width: 72 bits
        Data Width: 64 bits
        Size: 16384 MB
        ...
    > dmidecode -q -t 17 |grep Size
        Size: 16384 MB
        Size: 16384 MB
        Size: 16384 MB
        Size: 16384 MB
        Size: 16384 MB
        Size: 16384 MB
        Size: 16384 MB
        Size: 16384 MB
    ```

    ```sh
    > free -m
                total        used        free      shared  buff/cache   available
    Mem:         128526       88124       38120         132        2281       39136
    Swap:          2047        2044           3
    ```

-   查看硬盘信息。

    ```sh
    > fdisk -l |grep "Disk /dev/nvme"
    Disk /dev/nvme0n1: 477 GiB, 512110190592 bytes, 1000215216 sectors
    > fdisk -l |grep "Disk /dev/sd"
    Disk /dev/sda: 3.7 TiB, 4000787030016 bytes, 7814037168 sectors
    ```

    ```sh
    > df -h |grep "/dev/nvme"
    /dev/nvme0n1p1  469G  126G  320G  29% /
    > df -h |grep "/dev/sd"
    # note this hard disk has not mounted on the system
    ```

## dmidecode 指令

Linux 系统下可以用 `dmidecode` 指令获取有关硬件的信息。

该指令遵循 SMBIOS/DMI 标准，以一种可读的方式输出设备的 DMI（Desktop Management Interface）信息，其输出的信息包括 BIOS、系统、主板、处理器、内存、缓存等。

该指令可以查看到当前系统配置信息，也可以查看到系统支持的最大配置信息。

### 输出格式

`dmidecode` 指令输出的每条信息都具备如下格式。

```sh
Handle 0×0002, DMI type 2, 8 bytes
Base Board Information
	Manufacturer: Gigabyte Technology Co., Ltd.
	Product Name: X299-WU8-CF
	Version: x.x
	Serial Number: Default string
```

第一行是记录头（Record Header），包括：

-   Handle：DMI 表中的记录标识符。
-   DMI Type [Num]：记录类型标识符，如`type 2`表示 Base Board Information。
-   Record Size：记录大小，不包括文本信息，如`8 bytes`表示该记录占据 8 字节。

第二行是记录名称。

-   Record Name：记录名称，如 Base Board Information。

后面几行就是详细的记录信息。

### 全部信息

-   查看全部信息。

    ```sh
    # list all records
    dmidecode
    # list all records with less redundancy
    dmidecode [-q][--quite]
    ```

### 记录类型

-   所有记录包含以下的记录类型与相应标识符。可以在 `man dmidecode` 查看到。

    ```sh
    The SMBIOS specification defines the following DMI types:

    Type   Information
    ────────────────────────────────────────────
    0   BIOS
    1   System
    2   Baseboard
    3   Chassis
    4   Processor
    5   Memory Controller
    6   Memory Module
    7   Cache
    8   Port Connector
    9   System Slots
    10   On Board Devices
    11   OEM Strings
    12   System Configuration Options
    13   BIOS Language
    14   Group Associations
    15   System Event Log
    16   Physical Memory Array
    17   Memory Device
    18   32-bit Memory Error
    19   Memory Array Mapped Address
    20   Memory Device Mapped Address
    21   Built-in Pointing Device
    22   Portable Battery
    23   System Reset
    24   Hardware Security
    25   System Power Controls
    26   Voltage Probe
    27   Cooling Device
    28   Temperature Probe
    29   Electrical Current Probe
    30   Out-of-band Remote Access
    31   Boot Integrity Services
    32   System Boot
    33   64-bit Memory Error
    34   Management Device
    35   Management Device Component
    36   Management Device Threshold Data
    37   Memory Channel
    38   IPMI Device
    39   Power Supply
    40   Additional Information
    41   Onboard Devices Extended Information
    42   Management Controller Host Interface
    ```

### 按类型查询记录

-   可以按记录标识符查看记录。

    ```sh
    # list required record
    dmidecode -t [record_name][,record_name_2][...]
    dmidecode -t [record_id][,record_id_2][...]
    ```

## 查询固件指令汇总

-   查询系统固件信息。

    ```sh
    > cat /proc/version
    Linux version 5.4.0-42-generic (buildd@lgw01-amd64-023) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #46~18.04.1-Ubuntu SMP Fri Jul 10 07:21:24 UTC 2020
    ```

    ```sh
    > uname -a
    Linux server-442 5.4.0-42-generic #46~18.04.1-Ubuntu SMP Fri Jul 10 07:21:24 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
    ```

    ```sh
    > lsb_release -a
    No LSB modules are available.
    Distributor ID:	Ubuntu
    Description:	Ubuntu 18.04.5 LTS
    Release:	18.04
    Codename:	bionic
    ```
