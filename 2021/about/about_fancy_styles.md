# 启用 AutoStructify 额外样式

关于本文档提到，文档采用了 Sphinx 文档创建框架，其标记语言为 reStructuredText。通过 recommonmark 插件，可以让文档支持 Markdown 语法。

这里，我们再次引入 recommonmark 插件的另一部分，AutoStructify Component，使得使用 Markdown 语法编写的文档支持更多的 reStructuredText 语法的复杂样式。

## 为何引入

Markdown 语法具备简洁易用的特点，但 reStructuredText 语法具备了更为强大的功能，支持相当多更加复杂、可定制性更强的样式表达，例如醒目的提醒框、支持高亮的代码块、LaTeX 数学公式等等。

目前使用 sphinx_rtd_theme 主题呈现界面的一个明显问题在于，部分用于区分界面层级的元素的样式表达并不明确，例如引用语法，在该主题下仅有缩进效果，没有明显的颜色提示，表达样式容易引起混淆。为了使得文档界面更加易读，服务器文档使用 AutoStructify Component 来支持更多的表达样式（后续简称 ASC）。

这篇文档仅介绍插件的使用与部分实际使用到的样式。更加具体的说明，参见 recommonmark 插件的[文档](https://recommonmark.readthedocs.io/en/latest/index.html)。

## 使用 ASC

添加、配置、使用插件，以及具体语法说明。

### 修改配置文件

修改文档项目配置文件 `conf.py`，激活对应插件。需要进行以下三个步骤：

-   头部引入对应的模块；
-   在 `extensions` 字段写明具体的插件；
-   在 `setup` 函数定义插件的具体配置。

可供参考的配置文件如下：

```python
# conf.py
import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify

...

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "recommonmark",
]

...

# github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "enable_auto_toc_tree": True,
            "auto_toc_tree_section": "Contents",
            # "enable_auto_doc_ref": True,
            "enable_math": True,
            "enable_inline_math": True,
            "enable_eval_rst": True,
            # "url_resolver": lambda url: github_doc_root + url,
        },
        True,
    )
    app.add_transform(AutoStructify)
```

上述配置内容中包含了所有 ASC 组件的配置选项。默认情况下，这些选项都是启用的。通过显式声明的方式，可以对部分功能进行禁用。

```important:: 标准的 Markdown 语法并不支持代码高亮、LaTeX 公式或其他高级样式。

```

习惯使用所见即所得的 Markdown 编辑器 [Typora](https://typora.io/) 之后，会有一种 `.md` 文件支持代码块语法高亮、LaTeX 数学公式的错觉，实则不然。查阅 Markdown 语法[说明](https://markdown.com.cn/cheat-sheet.html)，才发现这些其实是 Typora 软件提供的额外渲染功能。

当然，通过 ASC，我们也可以在文档中实现类似的支持。

### 增强代码块语法

再次，Markdown 语法支持的仅仅是行内代码与代码块样式，并不支持具体的语法高亮。

-   在 ASC 中，简洁的代码块语法仅需要在常规语法之后写上具体语言即可，支持多数常见语言的语法高亮；
-   具体语言名称参见官方[文档](https://pygments.org/docs/lexers/)；
-   ⚠️ 不要保留语法标记与语言名称间的多余空格。

    ````
    ​```language
    some code block
    ​```
    ````

    例如，高亮 Python 代码块：

    ````
    ​```python
    def function():
        return True
    ​```
    ````

    将会得到如下渲染和高亮效果：

    ```python
    def function():
        return True
    ```

-   增强的语法表达中，可以指定代码块的显示样式，例如是否显示行号，高亮行等；
-   指定 `code-block` 关键字，其后添加代码语言名称;
-   ⚠️ 这里需要保留空格，对比上下差异；

    ````
    ```code-block:: md
        :linenos:
        :emphasize-lines: 3,5
        :caption: An example code-block with everything turned on.
        :name: Full code-block example

        # Comment line
        import System
        System.run_emphasis_line
        # Long lines in code blocks create a auto horizontal scrollbar
        System.exit!
    ```
    ````

    将会得到如下渲染和高亮效果：

    ```code-block:: md
        :linenos:
        :emphasize-lines: 3,5
        :caption: An example code-block with everything turned on.
        :name: Full code-block example

        # Comment line
        import System
        System.run_emphasis_line
        # Long lines in code blocks create a auto horizontal scrollbar
        System.exit!
    ```

```warning:: 通过 ASC 启用代码高亮样式，在源码中需要注意语法，尤其注意空格的保留。

```

### LaTeX 公式语法

数学公式语法与代码块类似。

-   行内公式：该版本并不支持，源码中出现 \$ 符号将会直接出现编译错误；
-   整行公式：使用 `math` 关键字的代码块。例如：

    ````
    ​```math
    E = m c^2
    ​```
    ````

    将会得到如下渲染和高亮效果：

    ```math
    E = m c^2
    ```

### 嵌入式结构文本语法

嵌入式结构文本能够带来更加精美的显示效果。

-   使用 `important`、`note`、`warning` 关键字得到不同颜色的嵌入式文本样式；
-   该嵌入式样式中不能继续嵌套更多的 Markdown 语法样式，包括所有行内样式；
-   ⚠️ 保留语法处空格。

    ````
    ​``` [important][note][warning]:: Its a note! in markdown!

    ​```
    ````

    将会得到如下渲染和高亮效果：

    ```important:: Its a note! in markdown!

    ```

    ```note:: Its a note! in markdown!

    ```

    ```warning:: Its a note! in markdown!

    ```

-   使用 `eval_rst` 关键字实现原生 reStructuredText 代码的转义，这一行为与多数语言支持的 `eval` 函数功能相同；
-   想要了解更多的 reStructuredText 语法，查阅官方[文档](https://docutils.sourceforge.io/docs/user/rst/quickref.html)。示例如下。

    ````
    ​```eval_rst
    .. autoclass:: recommonmark.transform.AutoStructify
        :show-inheritance:
    ​```
    ````

    将会得到如下渲染和高亮效果：

    ```eval_rst
    .. autoclass:: recommonmark.transform.AutoStructify
        :show-inheritance:
    ```

### 浮动边栏语法

浮动栏可以用作图片的插入框架。

-   使用 `sidebar` 关键字得到在右侧浮动的文本样式；
-   浮动样式会影响到周围的文本排版，其余文本会环绕在右侧浮动文本内容周围，参考 CSS 中的浮动样式；
-   该样式支持更多的 Markdown 语法内嵌。
-   ⚠️ 保留语法处空格，保留首行语法下的空行，注意源码缩进。

    ````
    ```sidebar:: Line numbers and highlights

        emphasis-lines:
            highlights the lines.
        linenos:
            shows the line numbers as well.
        caption:
            shown at the top of the code block.
        name:
            may be referenced with `:ref:` later.
    ```
    ````

    将会得到如下渲染和高亮效果：

    ```sidebar:: Line numbers and highlights

        emphasis-lines:
            highlights the lines.
        linenos:
            shows the line numbers as well.
        caption:
            shown at the top of the code block.
        name:
            may be referenced with `:ref:` later.
    ```
