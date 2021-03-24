# 服务器 Python 与 Anaconda 使用手册

实验室服务器使用 conda 的主要目的是区分不同用户的 python 环境，替代 virtualenv、pipenv 一类单独的环境管理工具。

前摇比较长，如果第一次使用，尽量仔细阅读，跟随指令步骤。

```note:: pip 它不香吗？

```

## 关于 Python

-   运行 Python 代码，或者.py 文件，只需要一个 Python 解释器，也即是常说的安装 Python 的直接对象。面对不同代码对环境的不同需求，可能需要不同版本的 Python 解释器，以及不同版本的第三方包，因此需要用不同的 Python 环境来进行区分。这里可以将环境理解为 Python 解释器与相关的第三方包的组合。
-   有很多种安装 Python 的方式。安装完成之后，Python 解释器的地址回被添加到系统的环境变量中，因此打开终端，输入`python3 --version`之后，终端知道找谁来解释这句指令，Python 解释器也会给出对应的输出。
-   可以在系统上安装各个版本的 Python 解释器。如果需要指定具体的版本，需要为终端或者 IDE 指定解释器的路径。修改系统的环境变量是一件麻烦的事情，因此使用环境管理器来更加方便地完成版本的安装和切换。

## 关于 Anaconda

-   [Anaconda](https://www.anaconda.com/) 附带了一大批常用数据科学包，它附带了 conda、Python 和 150 多个包及其依赖项。因此我们可以立即开始处理数据。这是用户一般使用 Anaconda 的主要原因，捆绑式地软件包使得环境配置相对轻松一些。
-   Python 默认的包管理器是 [pip](https://pip.pypa.io/)，此外还有很多衍生的包管理器，Anaconda 使用的就是其中的一种，称为 [conda](https://github.com/conda/conda)。其实 Anaconda 就是基于 conda 包管理器的一个衍生项目。当然，conda 也可以管理 Python 环境。
-   conda 可以兼容 pip 关于包的管理指令，但 conda 并不能完全兼容所有的 Python 第三方包。Anaconda 项目的目的是简化科学研究时环境的部署、管理问题，因此 conda 会聚焦在常用的科学研究处理方面的软件包及其依赖项。
-   因此，服务器配置 Anaconda 的主要目的是使用 conda 管理不同用户 Python 环境，而不是使用 conda 管理第三方包。用户可以根据自己的项目需求，使用 conda、pip 或是其他包管理器完成不同环境下第三方包的管理。
-   Anaconda 拥有一类机制，使得不同用户创建的环境可以共享第三方包的缓存。因此大家配置自己环境时，第三方包的安装配置过程将会非常迅速。

## 如何在服务器上管理自己的 Python 环境

登录到服务器之后，每个用户拥有自己的目录，位于`/home/username`。用户对于这个目录拥有完全的管理权限，因此所有活动都应该基于这一目录进行。用户目录之外的绝大多数位置，用户仅拥有读权限。

服务器上已经配置好了 Anaconda，它位于`/opt/anaconda`。用户组 anaconda 拥有这个目录的读与执行权限，默认新用户会加入该组。因此，所有用户都拥有`conda`指令的执行权限，但执行的更改内容仅限于自己的用户目录内部。

在服务器上，大家需要使用 conda 管理自己的 Python 环境。具体的步骤如下：

1. 初始化当前用户目录下的 conda；
2. 创建自己 Python 环境；
3. 切换到所需要的环境，安装第三方包，运行项目。

我们可以在自己的用户目录下创建无限多个 Python 环境。每一个环境内都可以指定 Python 的版本，以及其他第三方软件包的版本。创建的环境仅对于当前账户有效，其他账户并不会看见这个环境。因此不必担心自己的 Python 环境影响到服务器的 Python 环境，也不必担心其他用户影响到自己的环境。

## 初始化我的 conda

我们首次登录到服务器，运行 Python 项目之前，请先初始化环境管理器 conda。

-   `conda`指令对应的环境变量储存在`/etc/profile`中，为保证第一次登录后，可以正常使用`conda`指令，请使用`ssh name@100.64.198.24`的方式直接登录，而非在已登录其他账户的情况下，使用`su name`指令的方式切换账户。

-   可以使用`conda --version`来检测，当前账户是否可以正常使用 conda。

    ```sh
    # init conda env
    conda init zsh
    ```

-   conda 会修改当前账户的终端配置文件，使得所有`conda`指令生效。这一步是必须的，否则终端不能正确识别 conda 的所有指令。
-   务必使用 `zsh` 参数，所有服务器终端都应使用 zsh。

这里我们可以进一步配置自己的 conda，修改配置文件即可完成相应的配置。但如果没有特殊要求，使用默认的 conda 配置即可。

```note:: 初始化 conda 环境的过程只需要进行一次。

```

## 使用 conda 创建新的 Python 环境

-   初始化完成后，我们需要在自己的账户下创建自己的 Python 环境。

    ```sh
    # create new python env
    conda create -n [env_name] python=3.8
    ```

-   这里我们必须指明两个参数：

    -   `-n [env_name]`：环境名称。例如`-n env_std`，将会创建位于默认目录`~/.conda/envs`下，名称为`env_std`的 Python 环境。
    -   `python=3.8`：Python 版本。注意，只能指定第二级的版本，如`3.8`，不能指定更细致的版本号，conda 将会根据目前最近的子版本进行安装。
    -   环境名称可以根据需求自定义。Python 版本如无特殊需求，指定`3.8`版本。

```note:: 该指令中两个参数都必须指定，否则会造成创建的 Python 环境无效。

```

## 配置 Python 第三方包

配置第三方包的流程，`conda`指令与`pip`指令并无太大差异。但正如前面提到的，conda 没有包含所有的 Python 第三方包。因此，我们推荐始终使用 pip 来管理第三方包。

-   使用 pip 管理：

    ```sh
    # using pip
    pip list
    pip search [package_name]
    pip install [package_name]
    pip install --upgrade [package_name]
    pip uninstall [package_name]
    ```

-   使用 conda 管理：

    ```sh
    # using conda
    conda list
    conda search [package_name]
    conda install [package_name]
    conda update [package_name]
    conda remove [package_name]
    ```

## 快速迁移 Python 第三方包环境

如何快速迁移本机的 Python 第三方包到服务器创建的新环境？

-   手动记录重要的包环境，手动安装。
-   完整导出包环境列表文件，在服务器 Python 环境下利用该文件安装。

```note:: 更加推荐第一种方式，能尽量维持环境中仅出现需要的包。

```

可以使用如下步骤导出保环境列表文件，并利用文件进行安装：

-   使用 pip：

    ```sh
    # output package list file
    # on your pc
    pip freeze > ~/requirements.txt
    # on the server
    pip install -r ~/requirements.txt
    ```

-   使用 conda：

    ```sh
    # output package list file
    # on your pc
    conda list -e > ~/requirements.txt
    # on the server
    conda install --yes --file ~/requirements.txt
    ```

上述过程中需要注意文件的导出路径。复制文件到服务器后，同样需要注意文件的具体路径。

```note:: 再次，更加推荐第一种方式，能尽量维持环境中仅出现需要的包。

```

## 管理 conda 创建的 Python 环境

如果需要多个不同的 Python 环境，可以使用 conda 进行非常方便的管理。

-   查看当前账户拥有的环境：

    ```sh
    # list all envs
    conda info --envs
    conda info -e
    conda env list

    # sample output
    # conda environments:
    #
    old                      /home/zfj/.conda/envs/old
    std                   *  /home/zfj/.conda/envs/std
    base                     /opt/anaconda
    ```

    输出中，带`*`的环境表示当前激活，或正在使用的环境。

    所有用户都可以看到位于`/opt/anaconda`的`base`环境，这一环境为默认 conda 环境，请勿在该环境下运行 Python 项目或管理第三方包。

-   不同环境间的切换通过`activate`或`deactivate`进行：

    ```sh
    # switch to this env
    conda activate [env_name]
    # switch to default env
    conda deactivate
    ```

    默认环境是最近使用的、当前用户的环境；否则回退到`base`环境。

-   删除已创建的、不再需要的环境：

    ```sh
    # remove env by env_name
    conda remove -n [env_name] --all
    ```

    使用`--all`参数完成完整的删除。

-   创建与现有环境相同配置的环境，或复制环境：

    ```sh
    # create one same env
    conda create -n [env_name] --clone [existed_env_name]
    ```
