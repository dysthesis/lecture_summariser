These lecture notes provide a comprehensive summary of the topics discussed, drawing from both the lecture slides and the accompanying transcript. The content covers advanced Python functions, file handling, command-line argument parsing, package management, virtual environments, and an introduction to the `make` build tool.

### 1.0 Advanced Python Functions

This section revisits and expands upon the definition and usage of functions in Python, covering argument types, default values, variable arguments, scope, and anonymous functions.

#### 1.1 Function Definition and Invocation

Similar to the C programming language, Python functions can be defined with a fixed number of parameters. However, Python offers greater flexibility in how arguments are passed during function calls.

**Key Concept:**
A function is defined using the `def` keyword, followed by the function name and a list of parameters in parentheses.

```python
def polly(x, a, b, c):
    """calculate quadratic polynomial"""
    return a * x ** 2 + b * x + c
```

Functions can be invoked in several ways:
1.  **Positional Arguments:** Arguments are passed in the order they are defined in the function signature.
    ```python
    >>> polly(3, 5, -3, 6)
    42
    ```
2.  **Keyword Arguments:** Arguments are passed by explicitly naming the parameter. The order of keyword arguments does not matter.
    ```python
    >>> polly(a=5, c=6, b=-3, x=3)
    42
    ```
3.  **Mixed Arguments:** A combination of positional and keyword arguments can be used. All positional arguments must precede any keyword arguments.
    ```python
    >>> polly(3, c=6, b=-3, a=5)
    42
    ```

Additionally, special syntax (`/` and `*`) can be used in the function definition to enforce that certain arguments must be positional-only or keyword-only.

**Slide Cross-reference:** 2

#### 1.2 Default Argument Values

Function parameters can be assigned default values, making them optional during a function call.

**Key Concept:**
Default values are specified in the function definition using the assignment operator (`=`).

```python
def polly(x, a=1, b=2, c=0):
    return a * x ** 2 + b * x + c
```

This allows the function to be called with fewer arguments than defined; the default values are used for any omitted arguments.
```python
>>> polly(3)
15
>>> polly(b=1, x=1)
2
```

This feature is particularly useful for extending a function with new parameters without breaking existing code that calls it.

**Caveat: Mutable Default Parameters**
A significant pitfall in Python is the use of mutable types (e.g., lists, dictionaries) as default parameter values. The default value object is created only once, when the function is defined, and this single instance is used for all subsequent calls that omit the argument. This can lead to unexpected behaviour as modifications to the default object persist across calls.

**Example:**
The following function demonstrates this unintended side effect:
```python
def append_one(x = []):
    x.append(1)
    return x

>>> append_one()
[1]
>>> append_one()
[1, 1]
>>> append_one()
[1, 1, 1]
```

**Workaround:**
The standard practice to avoid this issue is to use `None` as the default value and then create a new mutable object inside the function if the argument is `None`.

```python
def append_one(x = None):
    if x is None:
        x = []
    x.append(1)
    return x

>>> append_one()
[1]
>>> append_one()
[1]
```

**Slide Cross-reference:** 3-6

#### 1.3 Variable Number of Arguments

Python functions can be defined to accept a variable number of arguments using the `*` and `**` operators.

**Key Concept:**
*   `*args`: Packs any excess positional arguments into a tuple.
*   `**kwargs`: Packs any keyword arguments that do not correspond to a formal parameter name into a dictionary.

**Example:**
```python
def f(*args, **kwargs):
    print('positional arguments:', args)
    print('keywords arguments:', kwargs)

>>> f("COMP", 2041, 9044, answer=42, option=False)
positional arguments: ('COMP', 2041, 9044)
keywords arguments: {'answer': 42, 'option': False}
```

The reverse operation, unpacking, can be used when calling a function.
*   `*iterable`: Unpacks an iterable (e.g., list, tuple) into positional arguments.
*   `**dictionary`: Unpacks a dictionary into keyword arguments.

**Example:**
```python
>>> arguments = ['Hello', 'there', 'Andrew']
>>> keyword_arguments = {'end' : '!!!\n', 'sep': ' --- '}
>>> print(*arguments, **keyword_arguments)
Hello --- there --- Andrew!!!
```

**Slide Cross-reference:** 7-8

#### 1.4 Variable Scope

Python's variable scope rules determine the visibility of a variable within a program.
*   A variable assigned a value within a function is **local** to that function by default.
*   A variable that is referenced but not assigned a value within a function is treated as a **global** variable (or a variable in an enclosing scope).
*   The `global` keyword can be used within a function to explicitly indicate that an assignment should modify a global variable, not create a new local one.

**Example:**
```python
x = 12

def f():
    x = 34  # Creates a new local variable 'x'
    print(x)

def g():
    global x # Refers to the global variable 'x'
    x = 56   # Modifies the global 'x'
    print(x)

>>> f()
34
>>> print(x) # Global x is unchanged
12
>>> g()
56
>>> print(x) # Global x is now changed
56
```

**A more complex example demonstrates lexical scoping:**
```python
# source code for scope.py
def a():
    x = 1
    # 'y' and 'z' are resolved from enclosing/global scopes.
    # 'y' is found in the global scope. 'z' was modified by c() and is global.
    print('a', x, y, z)

def b():
    x = 2
    y = 2
    a()
    print('b', x, y, z)

def c():
    x = 3
    y = 3
    global z
    z = 3
    b()
    print('c', x, y, z)

# Main execution
x = 4
y = 4
z = 4
c()
```
**Output:**
```
a 1 4 3
b 2 2 3
c 3 3 3
```

**Slide Cross-reference:** 11-13

#### 1.5 Anonymous Functions (`lambda`)

The `lambda` keyword is used to create small, anonymous functions. These are particularly useful in higher-order programming, such as when passing a simple function as an argument to another function (e.g., `map`, `filter`, `sorted`).

**Key Concept:**
A `lambda` function's body must be a single expression, and it cannot contain statements like `while` or `return`.

**Example:**
```python
>>> f = lambda x: x + 42
>>> type(f)
<class 'function'>
>>> f(12)
54
```

**Caveat: Late Binding of Variables**
Variables used in a `lambda` expression are bound at the time the function is *called*, not when it is *defined*. This is known as late binding.

**Example:**
```python
>>> answer = 42
>>> f = lambda x: x + answer
>>> answer = 15 # 'answer' is changed before 'f' is called
>>> f(12) # f(12) evaluates to 12 + 15
27
```

**Workaround:**
To capture the value at definition time, you can use a default argument, which is evaluated when the function is defined.
```python
>>> answer = 42
>>> f = lambda x, y=answer: x + y # y captures the value of 'answer' at definition time
>>> answer = 34
>>> f(12) # f(12) uses the default y=42, so evaluates to 12 + 42
54
```

**Slide Cross-reference:** 15-16

### 2.0 Functional Programming Constructs

Python includes several built-in functions and language features that support a functional programming style, enabling concise and expressive code.

#### 2.1 List Comprehensions

List comprehensions provide a concise syntax for creating lists from other iterables. They are often more readable than equivalent `for` loops.

**Syntax:**
*   `[expression for value in iterable]`
*   `[expression for value in iterable if condition]`

**Examples:**
```python
# Create a list of cubes for numbers 0-9
>>> [x**3 for x in range(10)]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Create a list of cubes for odd numbers 0-9
>>> [x**3 for x in range(10) if x % 2 == 1]
[1, 27, 125, 343, 729]
```

Nested list comprehensions are possible but can become difficult to read and may be better expressed using traditional loops.

**Example: Extracting Odd Numbers**
A function to extract odd numbers can be implemented using a standard loop or a list comprehension.
```python
def is_odd(number):
    return number % 2 == 1

# Using a for loop
def odd0(numbers):
    odd_numbers = []
    for n in numbers:
        if is_odd(n):
            odd_numbers.append(n)
    return odd_numbers

# Using a list comprehension
def odd1(numbers):
    return [n for n in numbers if is_odd(n)]
```
The list comprehension version is more compact and often considered more "Pythonic" for this type of task.

**Slide Cross-reference:** 14, 20

#### 2.2 Higher-Order Functions (`map`, `filter`, `sorted`)

Higher-order functions are functions that take other functions as arguments or return them as results.

##### 2.2.1 `map()`
The `map(function, iterable, ...)` function applies `function` to every item of `iterable` and returns an iterator of the results.

**Examples:**
```python
>>> list(map(str, range(10)))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> list(map(lambda x: x**3, range(10)))
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

##### 2.2.2 `filter()`
The `filter(function, iterable)` function constructs an iterator from elements of `iterable` for which `function` returns `True`.

**Example:**
```python
>>> list(filter(lambda x: x % 2 == 0, range(10)))
[0, 2, 4, 6, 8]
```
Similar to `map`, `filter` returns an iterator, which is a memory-efficient object that generates values on demand rather than creating a complete list at once. This allows it to work with very large or even infinite sequences.

##### 2.2.3 `sorted()` with a `key`
The `sorted(iterable, key=function)` function sorts the items of an iterable. The optional `key` argument specifies a function to be called on each list element prior to making comparisons. The return value of the key function is used as the basis for sorting.

**Example: Sorting Days of the Week**
To sort a list of day names chronologically instead of alphabetically, a key function can be used.

```python
# source code for sort_days.py
DAY_LIST = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split()
# Create a dictionary mapping day names to numbers 0-6
DAY_NUMBER = dict((day, number) for number, day in enumerate(DAY_LIST))

def sort_days0(day_list):
    # Use a lambda function to look up the day's number in the dictionary
    return sorted(day_list, key=lambda day: DAY_NUMBER[day])

def sort_days1(day_list):
    # Pass the dictionary's .get method directly as the key function
    return sorted(day_list, key=DAY_NUMBER.get)
```
Both `sort_days0` and `sort_days1` achieve the same result. The second version is slightly more concise by leveraging the fact that a dictionary's `get` method is a function that can be passed as the key.

**Slide Cross-reference:** 21, 23, 25

### 3.0 Program Structure and File Handling

This section covers structural aspects of Python programs, including the entry point for execution, documentation, and best practices for file I/O operations.

#### 3.1 Program Entry Point (`__name__ == '__main__'`)

Python does not have a special `main()` function like C or Java. When a Python file is executed, the interpreter runs the code in the file from top to bottom. This includes executing any code at the top level (i.e., not inside a function or class).

When a file is imported as a module into another file, its code is also executed. To distinguish between direct execution and importation, Python provides a special built-in variable `__name__`.
*   If the file is run directly, `__name__` is set to the string `"__main__"`.
*   If the file is imported, `__name__` is set to the module's name (the filename without the `.py` extension).

This allows for the creation of a conventional entry point for a script.
```python
def initial_function():
    # Main logic of the script
    print("Script is running directly.")

if __name__ == '__main__':
    initial_function()
```
Code within this `if` block will only run when the script is executed directly, not when it is imported as a module.

**Slide Cross-reference:** 9

#### 3.2 Docstrings

A docstring is a string literal that appears as the first statement in a module, function, class, or method definition. It is used to document what the object does.

**Key Concept:**
Docstrings are typically enclosed in triple quotes (`"""..."""` or `'''...'''`) to allow for multi-line strings. They are accessible at runtime through the object's `__doc__` attribute and are used by tools like `help()` and auto-documentation generators.

**Example:**
```python
def polly(x, a, b, c):
    """calculate quadratic polynomial

    a -- squared component
    b -- linear component
    c -- offset
    """
    return a * x ** 2 + b * x + c

>>> print(polly.__doc__)
calculate quadratic polynomial

    a -- squared component
    b -- linear component
    c -- offset
```

**Slide Cross-reference:** 10

#### 3.3 Safe File Modification Practices

When modifying a file, it is dangerous to read from and write to the same file simultaneously, as this can lead to data corruption or complete data loss.

**Incorrect Approach (Dangerous):**
Reading from a file and writing back to it within the same `open()` context.
```python
with open('pride-and-prejudice.txt', 'r+') as f:
    text = f.read()
    # ... perform modifications on text ...
    f.seek(0)
    f.write(modified_text) # This can truncate the file if modified_text is shorter
```

**Recommended Practices:**
1.  **Read all content into memory, then write.** If the file is small enough to fit into memory, this is the simplest approach.
    ```python
    # Read the entire file into a string
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Perform modifications
    changed_text = text.replace('Darcy', 'Elizabeth') # (Example)

    # Write the modified content back to the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(changed_text)
    ```

2.  **Use a temporary file.** For larger files, or for increased safety, write the modified content to a new temporary file. Once complete, replace the original file with the temporary one.
    *   **Atomic Rename:** The `os.rename()` operation is atomic on most systems if the source and destination are on the same filesystem. This means the replacement happens instantly, preventing race conditions where other processes might see an incomplete file.
    *   **Robust Move:** `shutil.move()` is a more robust alternative that can handle moves across different filesystems (by performing a copy then a delete), although it may lose the atomicity guarantee.

**Example using `os.rename`:**
```python
import os
import shutil

filename = 'pride-and-prejudice.txt'
temp_filename = filename + '.new'

with open(filename, 'r') as infile, open(temp_filename, 'w') as outfile:
    for line in infile:
        # process line
        outfile.write(processed_line)

# Atomically replace the original file with the new one
os.rename(temp_filename, filename)
```
For security, especially in multi-user environments, the `tempfile` module should be used to create temporary files with secure, unpredictable names.

#### 3.4 Command-Line Argument Parsing with `argparse`

The `argparse` module is the standard and recommended way to parse command-line arguments in Python. It automatically generates help and usage messages and issues errors when users give the program invalid arguments.

**Example:** A script `rename_regex.py` that renames files using a regular expression.
```python
import argparse
import sys
import re
import os

# Create the parser
parser = argparse.ArgumentParser(description='Rename files using regex.')

# Add arguments
parser.add_argument('regex', help='The regular expression to match.')
parser.add_argument('replacement', help='The replacement string.')
parser.add_argument('files', nargs='*', help='Files to rename.') # 0 or more files
parser.add_argument('-d', '--dry-run', action='store_true', help='Show what would be done, but do not rename files.')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')

# Parse arguments
args = parser.parse_args() # Looks at sys.argv by default

for old_pathname in args.files:
    new_pathname = re.sub(args.regex, args.replacement, old_pathname)
    if new_pathname != old_pathname:
        if args.verbose or args.dry_run:
            print(f"renaming '{old_pathname}' to '{new_pathname}'")
        if not args.dry_run:
            os.rename(old_pathname, new_pathname)
```
`argparse` handles:
*   Defining positional and optional arguments.
*   Specifying argument types, actions (e.g., `store_true`), and help text.
*   Parsing `sys.argv` into a structured object (`args`).
*   Automatically generating a `-h`/`--help` message.

### 4.0 Python Modules and Packages

This section introduces Python's ecosystem for code organization and distribution, including modules, packages, `pip`, and virtual environments.

#### 4.1 Modules and Packages

*   **Module:** A single Python file (`.py`) containing definitions and statements.
*   **Package:** A collection of modules organized in a directory hierarchy. A directory must contain an `__init__.py` file (which can be empty) to be considered a package.

#### 4.2 The Python Package Index (PyPI) and `pip`

*   **PyPI (Python Package Index):** The official third-party software repository for Python. It hosts hundreds of thousands of packages created by the community.
*   **`pip`:** The standard package installer for Python. It searches PyPI for packages and manages their installation, uninstallation, and updates.

**Caveat:** While PyPI is an invaluable resource, users should be cautious. Malicious packages have been found on PyPI in the past. It is advisable to only install packages from trusted sources, especially in security-sensitive environments.

#### 4.3 Virtual Environments

A virtual environment is an isolated Python environment that allows packages to be installed for a specific project, rather than being installed system-wide. This is the recommended practice for all Python development.

**Benefits:**
*   **Dependency Management:** Avoids conflicts where different projects require different versions of the same package (the "dependency hell" problem).
*   **Permissions:** Does not require administrator privileges to install packages.
*   **Reproducibility:** Ensures that a project has a clean, self-contained set of dependencies, which can be easily replicated by other developers.

**Creating and Using a Virtual Environment:**
1.  **Create the environment:**
    ```bash
    python3 -m venv my_project_env
    ```
    This creates a directory `my_project_env` containing a new Python installation.

2.  **Activate the environment:**
    *   On Linux/macOS:
        ```bash
        source my_project_env/bin/activate
        ```
    *   On Windows:
        ```batch
        my_project_env\Scripts\activate
        ```
    Once activated, your shell's prompt will change, and commands like `python` and `pip` will now refer to the versions inside the virtual environment.

3.  **Deactivate the environment:**
    ```bash
    deactivate
    ```

#### 4.4 Managing Dependencies with `requirements.txt`

It is standard practice to list a project's dependencies in a `requirements.txt` file.
*   **`pip freeze`**: Generates a list of all installed packages and their exact versions in the current environment.
    ```bash
    pip freeze > requirements.txt
    ```
*   **`pip install -r`**: Installs all packages listed in a given requirements file.
    ```bash
    pip install -r requirements.txt
    ```

A `requirements.txt` file can contain simple package names or specify version constraints:
```
# requirements.txt
requests
beautifulsoup4>=4.9.0,<5.0
django==3.2.12
```

### 5.0 Introduction to the `make` Build Tool

`make` is a classic and widely used build automation tool that is not specific to any programming language. It is primarily used to control the process of building executables and other non-source files from source code.

**Key Concepts:**
*   **Makefile:** A file (typically named `Makefile` or `makefile`) that contains the rules for building the project.
*   **Rule:** A rule specifies a target, its dependencies, and the commands to execute to create the target.
    ```make
    target: dependency1 dependency2 ...
        command1
        command2
    ```
*   **Dependency Checking:** `make` efficiently rebuilds the system by checking the modification timestamps of files. A target is rebuilt only if it does not exist or if any of its dependencies have been modified more recently than the target itself.

**Example `Makefile` for a C project:**
```make
# A simple Makefile for a multi-file C program.
CC=gcc
CFLAGS=-Wall

dominate: main.o graphics.o world.o
    $(CC) $(CFLAGS) -o dominate main.o graphics.o world.o

main.o: main.c graphics.h world.h
    $(CC) $(CFLAGS) -c main.c

graphics.o: graphics.c graphics.h
    $(CC) $(CFLAGS) -c graphics.c

world.o: world.c world.h
    $(CC) $(CFLAGS) -c world.c

clean:
    rm -f dominate *.o
```

When you run `make`, it reads the `Makefile`, determines the dependency graph, and executes the necessary commands to bring all targets up-to-date. If you run `make` again without changing any files, it will report that everything is up-to-date and do nothing, demonstrating its efficiency.

Further exploration of `make`, including an implementation of its core logic in Python, will be covered in subsequent lectures.

