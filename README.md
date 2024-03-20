# PySniper Package README

## Overview

PySniper is a powerful Python package designed to enhance debugging and code inspection. It allows developers to trace the execution of their Python code in real time, providing detailed insights into code behavior, variable changes, and execution paths. This document outlines the functionality, usage, examples, and output interpretation for the PySniper package.

Based on [pysnooper](https://github.com/cool-RR/PySnooper).

## Features

- **Real-time Code Tracing:** Monitor the execution of your code as it happens, with detailed insights into each step.
- **Variable Tracking:** Keep an eye on when and how your variables change throughout the execution.
- **Custom Callbacks:** Implement custom callback functions to handle different code events, such as new variables being created, variables being modified, or the execution moving to a new line of source code.
- **Color-coded Output:** Utilize colored output in your terminal to easily distinguish between different types of code events.

## Installation

Before using PySniper, you need to install it along with its dependencies. You can install PySniper using pip:

```sh
pip install pysniper
```

To use the color-coded output feature, you also need to install `termcolor`:

```sh
pip install termcolor
```

## Usage

To use PySniper in your project, you need to import the `snoop` decorator from the `pysniper` package and optionally, the `colored` function from `termcolor` if you want colored output.

Here's a basic setup:

```python
from pysniper import snoop, CodeEvent
from termcolor import colored
```

Next, define a callback function that will handle the code events emitted by PySniper. This function can print out the events, variables, and values in a color-coded format for better readability:

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

To trace a function, decorate it with `@snoop`, passing the path to a log file and the callback function:

```python
@snoop('test.log', callback=callback)
def test_func(count):
    # Your function code here
```

## Example

Consider the following function that counts from 0 to 10, appending each number to a list:

```python
if __name__ == "__main__":
    result = test_func(0)
```

### Output

When you run the script, PySniper generates a real-time, color-coded trace of the function execution:

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

Each line represents a different event during the execution, such as the creation of a new variable (`NewVar`), modification of a variable (`ModVar`), or execution moving to a new source line (`NextSourceLine`).

## Conclusion

PySniper offers a unique approach to debugging and understanding Python code by providing real-time insights into code execution and variable changes. With custom callbacks and color-coded output, it enhances the debugging process, making it easier to identify issues and understand code behavior.