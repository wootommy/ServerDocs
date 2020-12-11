# Linux 文件权限管理

本文档介绍 Linux 系统中文件权限管理的基本内容。

文件权限是系统最底层安全设定方法之一，它保证文件可以被可用的用户做相应操作。通过对文件设定权限可以达到以下三种访问限制权限：

-   只允许用户自己访问；
-   允许一个预先指定的用户组中的用户访问；
-   允许系统中的任何用户访问。

```important:: 设置文件权限管理是出于系统安全考虑，在所有操作系统中都有类似策略的不同实现。

```

## 文件，权限，拥有者

我们先展开介绍一下一些关键的概念，进一步了解文件权限管理的意义。

对于任意的文件或文件夹，可以使用 `ls -l [filename]|[dirname]` 查看其具体信息。`ls -l` 表示展开为表格形式（list）。

这将会得到类似如下的输出：

```sh
~ > ls -l
drwx------@ - tommy 28 Oct 12:21 Applications
drwx------@ - tommy 10 Dec 17:18 Desktop
drwx------@ - tommy 11 Dec  9:49 Documents
drwx------  - tommy 11 Dec 14:07 Downloads
```

### 文件类型

Linux 系统中包括 2 种基本的文件类型，5 种特殊的文件类型。

| 文件属性 | 文件类型                                                             |
| -------- | -------------------------------------------------------------------- |
| -        | 常规文件，如包纯文本文件，二进制文件；数据格式的文件，各种压缩文件等 |
| d        | 目录文件，可以通过 `cd` 指令进入                                     |
| b        | 块设备文件，来自存储数据以供系统存取的接口设备，简单说就是硬盘       |
| c        | 字符设备文件，来自串行端口的接口设备，例如键盘、鼠标、虚拟终端等     |
| l        | 符号链接文件，简单说就是替身，软链接，快捷方式                       |
| p        | 通过 FIFO 解决多个程序同时存取一个文件所造成的错误的缓存文件         |
| s        | 套接字文件，用于实现两个进程进行通信                                 |

```note:: 一般来说，我们只会接触到常规文件和目录文件。

```

### 文件所有者与所有组

对于每一个文件，可以按照文件所有者、文件所有组或其他用户组来分别配置文件权限。

-   **所有者**（owner）：文件的建立者。用户拥有对它所创建的文件的一切权限，所有者可以允许其所在的用户组可以访问所有者的文件。
-   **所有组**（group）：用户组是具有相同特征用户的逻辑集合。组内所有用户共享改组对文件的权限。
-   **其他用户组**（others）：除开所有者和所有组内所有用户的所有剩余用户的逻辑合集。

```note:: 系统中绝大多数系统文件都是由 root 建立的，所以大多数系统文件的所有者都是 root。

```

### 文件权限

对于每一个文件，有三种权限可以应用，分别是读取，写入与执行。

| 权限 | 含义    | 对常规文件（-） | 对目录文件（d）                    |
| ---- | ------- | --------------- | ---------------------------------- |
| r    | read    | 读取文件内容    | 读取目录中文件列表                 |
| w    | write   | 写入文件内容    | 创建、删除目录中文件，改变目录名称 |
| x    | execute | 执行该指令文件  | 进入该目录                         |

对于每一类用户，系统使用 3 位字符来表示权限设置。3 位字符可以按照二进制规则，从 3 位二进制数字表示转化为八进制 1 位数字表示。

| 权限 | 二进制 | 八进制 | 权限含义   |
| ---- | ------ | ------ | ---------- |
| ---  | 000    | 0      | 无权限     |
| r--  | 100    | 4      | 只读       |
| -w-  | 010    | 2      | 只写       |
| --x  | 001    | 1      | 仅执行     |
| rw-  | 110    | 6      | 读写       |
| r-x  | 101    | 5      | 读取或执行 |
| -wx  | 011    | 3      | 写入或执行 |
| rwx  | 111    | 7      | 所有权限   |

```note:: 一般使用八进制 1 位数来表示权限。

```

## 权限相关指令

### 查看权限

使用 `ls -l` 可以查看单一文件的权限，也可以查看目录下所有文件的权限。添加不同的参数即可。

-   查看单一文件权限：

    ```sh
    ls -l [filename]
    ls -ld # -d for list dir itself, current dir by default
    ls -ld [dirname] # set dir to [dirname]
    ```

-   查看目录下所有文件权限：

    ```sh
    ls -l # current dir by default
    ls -la # -a for hidden files
    ls -lD # -D for only dirs
    ls -l [dirname] # set dir to [dirname]
    ```

-   权限内容将以下述格式展开：

    ```sh
    drwxr-x---  2 root root       37 Apr 18 10:50 data
    -rw-r--r--  1 root root    68549 Sep 26  2018 fields.yml
    -rwxr-xr-x  1 root root 33903123 Sep 26  2018 filebeat
    -rwxr-xr-x  1 root root     1011 Mar 27 10:13 filebeat-docker.yml
    ```

这是一个文件信息的实例：

| 实例         | 片段     | 描述                                                          |
| ------------ | -------- | ------------------------------------------------------------- |
| d            | 文件类型 | 1 位字符表示文件类型，常见 `-` 或 `d`                         |
| rwxr-x---    | 文件权限 | 9 位字符表示文件权限，按所有者、所有组、其他用户组各 3 位展开 |
| 2            | 链接数量 | 对于文件，表示其软链接数量；对于目录，表示其子目录文件数量    |
| root         | 所有者   | 文件的所有者                                                  |
| root         | 所有组   | 文件的所有组                                                  |
| 37           | 文件大小 | 文件大小，单位为字节（byte）                                  |
| Apr 18 10:50 | 修改时间 | 最近一次的修改时间，以当前系统时间为标准                      |
| data         | 文件名   | 常规文件名含后缀，目录文件不含后缀                            |

```note:: 文件信息总是按照上述格式展开。

```

### 更改文件所有者和所有组

使用 `chown` 和 `chgrp` 改变文件的所有者和所有组。使用 `R` 选项进行递归更改，即改变将适用与目录下所有子文件。

-   修改文件所有者：

    ```sh
    chown [username] [filename]
    chown -R [username] [filename]
    ```

-   修改文件所有组：

    ```sh
    chgrp [groupname] [filename]
    chgrp -R [groupname] [filename]
    ```

-   同时修改所有者和所有组：

    ```sh
    chown [username]:[groupname] [filename]
    chown -R [username]:[groupname] [filename]
    ```

注意，必须是文件所有者才可以更改文件所有者或所有组。这些指令不会有明显的输出，除非触发了权限错误（permission denied）。再次使用 `ls -l` 查看文件更新后的权限。

### 修改文件的权限

使用 `chmod` 进行文件权限的修改。使用 `R` 选项进行递归更改，即改变将适用与目录下所有子文件。

-   使用权限的字符表示进行设定：

    ```sh
    chmod [object_group][operator][permisson_combination] [filename]
    chmod -R [object_group][operator][permisson_combination] [filename]
    ```

    这里的对象组合是指 `u`、`g`、`o`、`a`，分别表示所有者即用户（user）、所有组（group）、其他用户组（others）、所有用户（all）至少一位的组合；权限操作符包括 `+`、`-`、`=`，分别表示添加、去除和指定后面的权限组合；权限组合则是 `r`、`w`、`x` 至少一位的任意组合。

-   使用权限的数字表示进行设定：

    ```sh
    chmod [permisson_combination] [filename]
    ```

    这里权限组合是固定三位、八进制权限表示的组合。每一位按序依次表示所有者、所有组、其他用户组的权限。

-   这里有一些修改文件权限的示例：

    ```sh
    chmod g+w demo.txt
    chmod a+w demo.txt
    chmod o-w demo.txt

    chmod go+r demo.txt
    chmod ug=rwx script.py
    chmod a=rw demo.text

    chmod 764 scirpt.py
    chmod 700 demo.txt
    chmod 766 demo.txt
    ```

```warning:: 文件所有者总是对文件保持所有权限，无论如何进行设置。注意，是当前文件的所有者，而非文件初始的创建者。

```