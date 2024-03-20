# PySniper 包 README

## 概览

PySniper 是一个强大的 Python 包，旨在增强调试和代码检查能力。它允许开发者实时追踪他们的 Python 代码执行情况，提供代码行为、变量变化和执行路径的详细洞察。本文档概述了 PySniper 包的功能、使用方法、示例以及输出解释。

基于 [pysnooper](https://github.com/cool-RR/PySnooper)。

## 特性

- **实时代码追踪：** 实时监控代码执行情况，提供每一步的详细洞察。
- **变量跟踪：** 监控变量在执行过程中的变化情况。
- **自定义回调：** 实现自定义回调函数来处理不同的代码事件，如创建新变量、修改变量或执行移至新的源代码行。
- **彩色输出：** 在终端中使用彩色输出，以便轻松区分不同类型的代码事件。

## 安装

在使用 PySniper 之前，你需要安装它及其依赖。可以使用 pip 安装 PySniper：

```sh
pip install pysniper
```

如果你想要彩色输出功能，还需要安装 `termcolor`：

```sh
pip install termcolor
```

## 使用方法

要在项目中使用 PySniper，需要从 `pysniper` 包导入 `snoop` 装饰器，如果需要彩色输出，还需从 `termcolor` 导入 `colored` 函数。

基本设置如下：

```python
from pysniper import snoop, CodeEvent
from termcolor import colored
```

接下来，定义一个回调函数来处理 PySniper 发出的代码事件。这个函数可以以彩色格式打印事件、变量和值，以提高可读性：

```python
def callback(code_event: CodeEvent, locals: dict, *args, **kwargs):
    match code_event:
        case CodeEvent.NewSourcePath:
            print(colored(f"{code_event}, {kwargs['source_path']}", 'blue'))
        case CodeEvent.NewVar:
            print(colored(f"{code_event}, {kwargs['var_name']} = {kwargs['var_value']}", 'yellow'))
        case CodeEvent.ModVar:
            print(colored(f"{code_event}, {kwargs['var_name']} = {kwargs['var_value']}", 'green'))
        case CodeEvent.NextSourceLine:
            print(colored(f"{code_event}, {kwargs['source_line']}", 'cyan'))
```

要追踪一个函数，请用 `@snoop` 装饰它，并传入日志文件的路径和回调函数：

```python
@snoop('test.log', callback=callback)
def test_func(count):
    # 函数代码
```

## 示例

考虑以下从 0 数到 10 的函数，将每个数字添加到列表中：

```python
if __name__ == "__main__":
    result = test_func(0)
```

### 输出

当你运行脚本时，PySniper 生成函数执行的实时彩色追踪信息：


```
CodeEvent.NewSourcePath, pysniper/test_tracer.py
CodeEvent.NewVar, count = 0
CodeEvent.NextSourceLine, def test_func(count):
CodeEvent.NextSourceLine,     x = []
CodeEvent.NewVar, x = []
CodeEvent.NextSourceLine,     while count < 10:
CodeEvent.NextSourceLine,         count += 1
CodeEvent.ModVar, count = 1
CodeEvent.NextSourceLine,         x.append(count)
CodeEvent.ModVar, x = [1]
CodeEvent.NextSourceLine,     while count < 10:
CodeEvent.NextSourceLine,         count += 1
CodeEvent.ModVar, count = 2
CodeEvent.NextSourceLine,         x.append(count)
CodeEvent.ModVar, x = [1, 2]
CodeEvent.NextSourceLine,     while count < 10:
CodeEvent.NextSourceLine,         count += 1
CodeEvent.ModVar, count = 3
CodeEvent.NextSourceLine,         x.append(count)
CodeEvent.ModVar, x = [1, 2, 3]
...
CodeEvent.NextSourceLine,     y = x.pop()
CodeEvent.ModVar, x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CodeEvent.NewVar, y = 10
CodeEvent.NextSourceLine,     return y
CodeEvent.NextSourceLine,     return y
```


每行代表执行过程中的不同事件，如新变量的创建（`NewVar`）、变量的修改（`ModVar`）或执行移至新源代码行（`NextSourceLine`）。

## 结论

PySniper 通过提供实时的代码执行和变量变化洞察，为调试和理解 Python 代码提供了独特的方法。通过自定义回调和彩色输出，它增强了调试过程，使识别问题和理解代码行为变得更加容易。