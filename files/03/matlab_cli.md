# 终端运行 Matlab 使用手册

Matlab 本身是一个强图形化界面依赖的程序，但跟所有软件一样，图形界面只是指令集合（可执行指令集）的外包装，Matlab 同样可以通过终端运行，执行对应文件的内容并显示输出。

这份手册简要介绍一下终端操作 Matlab 的方法。

```note:: Matlab 同样支持在终端执行，管理员需要手动链接可执行文件到环境变量。

```

## 欢迎来 442 写代码

在开始介绍之前，大家需要了解的是，阿圆学长（nami-442@hpc）已经在 442 写过累计超过 40 小时工作量的代码。

是的，如果出现各种教程与意料之外的情况，眼前又有迫切需要完成的 Matlab 项目，欢迎大家直接来到 308，在服务器本机上完成项目代码的编译与运行工作。

```note:: 👍 这绝对是最为保险的做法。

```

## 矛盾的权限问题

在具体的使用方式之前，管理员有必要了解关于 Matlab 可执行程序的一些权限问题。

目前，服务器有三类按权限区分的用户：

-   root：系统最高权限账户，唯一，不可篡改；
-   nami-442: 管理员账户，设置为唯一，可修改；
-   username：普通账户，不唯一，可修改。

在 Matlab 安装与激活的过程中，为了省去不必要的权限问题（包括 Matlab 安装时创建文件与软连接的权限），全程使用了管理员账户进行安装、授权激活。

而目前，Matlab 在启动时会检测当前执行账户是否为激活时账户。这意味着，即便创建了拥有权限的用户组，普通用户仍然不能通过自己的账户执行 Matlab 程序；而当初安装激活时，普通用户并不能顺利地完成安装过程。

```warning:: 除非精心设计好一个拥有安装过程所需权限、又不具备管理员权限的特殊普通账户，否则目前来说，只能使用管理员账户打开 Matlab。⚠️ 这是一个潜在的危险。

```

## Matlab 环境变量

早期的 Matlab 安装完成后（实测包活 R2020a 之前版本），可能需要手动在环境变量中添加 Matlab 可执行程序，或者在终端配置文件中添加快捷方式，直接导入可执行文件路径。

-   添加可执行文件路径；

    ```sh
    # matlab
    alias matlab="sudo /usr/local/bin/matlab"
    ```

-   验证终端是否识别 Matlab 指令。

    ```sh
    nami-442@server-442:~$ which matlab
    /usr/local/bin/matlab
    ```

## `matlab`指令

当管理员准备就绪之后，我们可以使用 SSH 登录的方式，在终端使用 Matlab。

### 查看指令帮助

-   使用`matlab -h[-help]`查看所有的指令参数；

    ```sh
    nami-442@server-442:~$ matlab -h

        Usage:  matlab [-h|-help] | [-n | -e]
                       [v=variant]
                       [-c licensefile] [-display Xdisplay | -nodisplay]
        ...
    ```

-   比较重要的几个参数如下。可以在[这里](https://ww2.mathworks.cn/help/matlab/ref/matlabmacos.html)找到更为详细的说明。

    ```sh
    ...
        -nodisplay              - Do not display any X commands. The MATLAB
                                  desktop will not be started. However, unless
                                  -nojvm is also provided the Java virtual machine
                                  will be started.
        -nosplash               - Do not display the splash screen during startup.
        -nodesktop              - Do not start the MATLAB desktop. Use the current
                                  terminal for commands. The Java virtual machine
                                  will be started.
        -r MATLAB_command       - Start MATLAB and execute the MATLAB_command.
                                  Cannot be combined with -batch.
        -logfile log            - Make a copy of any output to the command window
                                  in file log. This includes all crash reports.
    ...
    ```

### 常用的指令形式

如果没有特殊要求，可以使用如下推荐的指令形式。默认情况下，使用该指令运行单一的`.m`文件。

-   适用于终端 SSH 连接启动的 Matlab；

    ```sh
    matlab -nodesktop -nodisplay -nosplash -r [matlab_file]
    ```

-   适用于终端 SSH 连接启动的 Matlab（包含日志）；

    ```sh
    matlab -nodesktop -nodisplay -nosplash -logfile `matlab_log_%Y_%m_%d-%H_%M_%S`.log -r [matlab_file]
    ```

-   如果需要交互代码式执行，无需添加文件路径。

    ```sh
    matlab -nodesktop -nodisplay -nosplash
    ```

    交互式界面如下：

    ```sh
    nami-442@server-442:~$ matlab -nodesktop -nodisplay -nosplash

                                        < M A T L A B (R) >
                            Copyright 1984-2020 The MathWorks, Inc.
                        R2020a Update 2 (9.8.0.1380330) 64-bit (glnxa64)
                                            May 5, 2020


    To get started, type doc.
    For product information, visit www.mathworks.com.
    >>
    ```

```note:: 这些指令禁用了 Matlab 的图形化界面与相关输出，适用于终端。

```

大家应始终注意：

-   在正确的路径下运行指令，或在指令中指定正确的路径；
-   程序若有文件的读取与保存，同样要设置好相关路径；
-   在`.m`源文件中设置好关键位置的输出，方便在终端查看到目前执行的进度；
-   不要使用`nohup`之类的指令使得 Matlab 始终保持在后台运行，它的占用消耗比较大；
-   使用日志文件可以帮助你了解程序中的关键信息，即使不小心退出了终端、意外关闭连接。

```warning:: 再次，指定正确的路径非常重要。

```

### 退出指令环境

-   使用`exit`即可。

    ```sh
    ...
    >> exit
    nami-442@server-442:~$
    ```
