# 关于本文档

如果有小伙伴好奇这个文档是怎么搭建起来的，这里做一个简单的介绍。

我们使用的是 Read the Docs，一个免费的在线文档托管系统，[官网](https://readthedocs.org/)。托管文档的基本流是 Sphinx + GitHub + ReadtheDocs，即 Sphinx 作为编辑器框架生成与撰写文档，GitHub 作为仓库存放文档，再导入到 ReadtheDocs 进行托管。

## Sphinx

Sphinx 是一个文档创建的框架工具，可以轻松创建智能、美观的文档。它最开始只用来写 Python 文档，后来渐渐发展成熟。其使用`reStructuredText`作为其标记语言，具备强大的解析性，另外的一些相关套件可以提供强大的翻译特性。

### 初始化项目

-   基于 Python。
-   使用指令`sphinx-quickstart`初始化一个标准的文档项目。
-   初始化过程步骤，第一项务必选择 no。
-   `conf.py`用于定义项目基本配置，可编辑；`index.rst`用于定义呈现出来的文档结构，可编辑。

```bash
# install with pip3
pip install sphinx sphinx-rtd-theme sphinx-autobuild recommonmark

# quick init one docs project
sphinx-quickstart

# quick init steps
> Separate source and build directories (y/n) [n]: n # must be no
> Project name: Demo Prj
> Author name(s): tommy
> Project release []:
> Project language [en]:
```

-   初始的项目结构。

```bash
# init prj tree
# 3 directories, 4 files
.
├── Makefile  # auto file
├── _build # output dir
├── _static # figs, codes...
├── _templates # temps
├── conf.py # conf.py, important
├── index.rst # index.rst, important
└── make.bat # auto file

# if separate build and source dir
# 4 directories, 4 files
.
├── Makefile
├── build
├── make.bat
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
```

### 定义文档结构

`index.rst`也被称为`mastar-document`，是文档的主入口，或者说默认的起始页。起始页一般包含的是整个文档的目录，当然也可以自定一比较完善的其他结构。

-   整个文档可以自定义，但必须包含`toctree::`指令。
-   指令指的是 reStructuredText 的语法以及 Sphinx 为其添加的语法。例如下面`..`就是注释开头，`.. Command::`是指令的基本结构，`*`是无序列表，`:ref:`term``是索引跳转链接。
-   `toctree::`指令决定了右侧目录显示哪些层级、文件。显示的名称由文件的主标题决定。

```md
.. here's some init comments

# Welcome to Demo Prj's documentation!

.. toctree::
:maxdepth: 2
:caption: Contents:

# Indices and tables

-   :ref:`genindex`
-   :ref:`modindex`
-   :ref:`search`
```

### 套用主题

`conf.py`是项目的配置文件。具体的配置项在里面有很详细的说明。

-   引入主题模块 sphinx_rtd_theme。可以在 PyPI[页面](https://pypi.org/project/sphinx-rtd-theme/)查询到模块介绍。
-   修改配置变量`extensions`和`html_theme`。

```python
# conf.py

import sphinx_rtd_theme
extensions = ["sphinx_rtd_theme", "recommonmark"]
html_theme = "sphinx_rtd_theme"
```

### 组织文档文件

文档文件可以放在根目录下的任意位置，在`toctree::`里面指定对应的路径即可。

-   建议文档文件`.md`都放在根目录`files`文件夹内。

```md
.. toctree::
:maxdepth: 2
:titlesonly:
:caption: Configuration

files/configuration/0x01
...
```

```bash
# dir structure
...
├── files
│   ├── configuration
│   │   ├── 0x01.md
│   │   ├── ...
│   │   └── 0x08.md
│   └── user_manual
│       └── manual_conda.md
...
```

### 支持`.md`文件

Sphinx 默认支持的文档文件是`.rst`，但可以使用第三方模块`recommonmark`使其支持`.md`文件。后者相对来说只是一种简单的兼容模式，前者的语法特性更加完善。

-   引入模块 recommonmark 即可。

```python
extensions = ["sphinx_rtd_theme", "recommonmark"]
```

-   另外，还可以该模块下的 AutoStructify，使得在 build 时，将`.md`文件转换为，`.rst`文件。感觉可以，但没必要。说明见[这里](https://github.com/readthedocs/recommonmark)。

### 编译项目

编译之后，产出文件将会出现在`_build`文件夹，用于本地预览。

-   可以使用两种编译指令。
-   编译的文件仅仅用于本地预览。在文件夹内找到`index.html`打开即可。

```bash
# using sphinx-build
sphinx-build -b html sourcedir builddir # -b [output_type]

# using make
make html
```

## Read the Docs

这个有点像之前的 Github Pages，都是托管站。可以理解为免费的服务器，链接到 GitHub 项目，利用项目生成对应内容发布到服务器，可以实现在线访问。所有过程都是自动、免费的。联想到之前实习时候的 CI/CD。

### 发布项目到 Github

-   添加对应的 gitignore 规则，无需上传输出文件夹`_build`。
-   项目可能需要一些额外的设置。主要在 Webhooks。如果默认配置不成功，需要手动添加新的 Webhook，具体的流程在 RtD 的管理面板也有。

### Read the Docs 管理面板

-   登录到管理面板[页面](https://readthedocs.org/dashboard/)。
-   导入新的项目。可以选取列表里列出的项目，或者手动进行导入。
-   导入成功后，项目会自动进行 build 与 release，一般在几分钟内就能够完成，可以在详情页面查看到 build 日志与相应的项目文档地址。
