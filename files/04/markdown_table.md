# 启用 Table 样式插件

这篇文档重新介绍一下如何在 Sphinx 框架中启用对 markdown 文件的支持，并添加支持表格的样式插件。

通过阅读前面的文档中，我们知道：

-   这份文档使用 Sphinx 框架生成；
-   在项目的的配置文件 `conf.py` 中通过启用 recommonmark 插件与其 AutoStructify Component 组件，使得项目支持直接从 markdown 格式（包括一些特殊的语法，如代码块高亮、LaTeX 公式与标注样式等等）直接转换生成对应的 reStructuredText 格式并最终转化为 html 文件输出；
-   通过配置单独的 css 文件修改少量的样式；
-   所有文档输出内容托管在 Read the Docs 网站上从而可以在互联网上进行访问。

但目前为止，我们写在 markdown 文件中的表格语法并不被框架直接支持，无法在 html 中输出表格。

## 为 recommonmark 安装支持的插件

我们可以通过安装新的插件，实现对 markdown 文件中表格语法的支持。这里，再次回顾一下在 Sphinx 框架中启用新插件的步骤。

首先，为了启用对表格语法的支持，我们需要找到对应的插件。目前推荐的插件是：sphinx-markdown-tables，它最近一次的更新在 20 年 6 月，[链接](https://pypi.org/project/sphinx-markdown-tables/)。

```note:: 这些步骤适用于一般的插件安装、启用过程。

```

-   框架本身以及插件都是 Python 环境下的第三方包，所有安装都使用 pip 进行。因此，我们首先需要使用 pip 安装这个插件到本地环境，方便本地构建预览版本。

    ```sh
    pip install sphinx-markdown-tables pymdown-extensions
    ```

    如果需要回忆一下，到目前位置我们一共安装了这些 Python 第三方包：

    ```sh
    > pip list
    ...
    recommonmark                  0.6.0
    Sphinx                        3.2.1
    sphinx-autobuild              2020.9.1
    sphinx-markdown-tables        0.0.15
    sphinx-rtd-theme              0.5.0
    ...
    ```

-   在 `conf.py` 中配置并启用新的插件。修改 `extensions` 字段后的列表即可，添加新的插件内容。

    ```py
    extensions = [
        "sphinx_rtd_theme",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.mathjax",
        "recommonmark",
        "sphinx_markdown_tables",
    ]
    ```

    注意到，其实我们仅仅启用了两个自定以的插件，一个是 recommonmark，一个是 sphinx_markdown_tables。它们都使用 pip 安装，都通过这样的方式启用。

    ```note:: 其他插件来自 Sphinx 自带的依赖库。

    ```

-   然后，我们就可以直接在 md 文件中，使用表格语法，它会自动通过以上两个插件转义成最后我们看到的表格。

    ```md
    | 表头 | 表头列 |
    | ---- | ------ |
    | 内容 | 内容   |
    ```

    这会渲染得到一下内容：

| 表头 | 表头列 |
| ---- | ------ |
| 内容 | 内容   |

-   需要注意的是，目前表格的渲染不支持缩进。请勿在 md 源文件中对表格语法进行缩进。源码内容无法对齐，因为中文字符与引文字符的宽度并不一致。

## 或者，更换转义的插件库

另一种思路是，完全使用另一种文件转义库（parser）。

recommonmark 本质上就是一种转义库，输入是 markdown 文件，输出是 rst 文件，但其默认情况下不支持一些 markdown 的扩展语法。为了支持其中的语法，我们为其启用 AutoStructify Component 组件，并在配置文件 `conf.py` 中进行相应的配置，就能使其在转义的过程中输出对应的、合理的 rst 内容。

除了为 recommonmark 启用另一种插件外，我们也可以完全使用另一种转义库。目前推荐的插件是：sphinx-markdown-parser 20 年 9 月，[链接](https://pypi.org/project/sphinx-markdown-parser/)

请参照官网步骤进行具体的配置。注意，只能为 Sphinx 启用一个转义 md 文件的转义库，因此 sphinx-markdown-parser 与 recommonmark 是互斥的，二选一。

```warning:: 这个项目目前并不是很完善，管理员在本地 build 总是失败，所以没有具体的过程介绍，详情参照官网。但这依然是一个不错的思路。

```

## 上传配置依赖文件

如果使用了 Sphinx 默认之外的第三方包，比如上述的 sphinx-markdown-tables 和 sphinx-markdown-parser，我们需要在针对托管服务的配置文件 `.readthedocs.yml` 中进行配置。否则，服务容器中不包含这些第三方包，在构建的过程中就会报错。

-   这是目前该项目所使用 yml 文件内容：

    ```yml
    # .readthedocs.yml
    # Read the Docs configuration file
    # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

    # --------------------------------- Required --------------------------------- #
    # V2 or V1
    version: 2

    # ---------------------- Build documentation with Sphinx --------------------- #

    sphinx:
        configuration: ./conf.py

    # ----------- Optionally set the version of Python and requirements ---------- #

    python:
        version: 3.8
        install:
            - requirements: ./requirements.txt

    # ------- Optionally build your docs in additional formats such as PDF ------- #

    formats: []
    ```

    注意，我们在 `python` 字段下配置了 `install - requirements` 字段，其指向一份具体的配置文件，它由本地的 pip 生成，我们需要把它放到项目中去。

-   这是一份示例的 txt 文件内容：

    ```txt
    recommonmark==0.6.0
    Sphinx==3.2.1
    sphinx-autobuild==2020.9.1
    sphinx-markdown-tables==0.0.15
    sphinx-rtd-theme==0.5.0
    ```

    通过在这里指定所依赖的 Python 包，托管服务器就可以在构建的时候正确地配置所需依赖。
