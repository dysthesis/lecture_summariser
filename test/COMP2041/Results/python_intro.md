Of course. Here is a comprehensive and detailed set of lecture notes based on the provided materials.

***

### **Lecture Notes: An Introduction to Python for Scripting and System Administration**

#### **1. Course Administration & Announcements**

These notes are compiled from lectures delivered at approximately the halfway point of the course, preceding and following a "Flexibility Week".

*   **Flexibility Week (Week 6):** There will be no lectures, tutorials, or labs for this course during Flexibility Week. This period is intended for students to work flexibly on course material, particularly Assignment 1. It is not a holiday.
*   **Assignment 1 (Shell Scripting):** The deadline for Assignment 1 is 9 a.m. on Monday of Week 7. Students are strongly encouraged to start early to avoid long queues at help sessions, which become exceedingly busy in the days leading up to the deadline. The standard UNSW late penalty applies.
*   **Assignment 2 (Python):** Assignment 2, which will focus on Python, is expected to be released shortly after the Assignment 1 deadline. It will be discussed in the Week 7 lecture.
*   **Lab Exercises:** To accommodate the assignment deadline, the lab exercises for Week 5 have been granted a one-week extension and are due on Monday of Week 7.
*   **Weekly Tests:**
    *   Weekly Test 2 was due on the evening of the Week 5 lecture.
    *   Weekly Test 3 will be released on the evening of the Week 5 lecture and will be due on Thursday of Week 7, providing a two-week window for completion.
    *   Another weekly test will be released during Flexibility Week, also due on Thursday of Week 7.
*   **Course Drop Deadline:** The deadline to drop a course without academic penalty (but with financial liability) is typically during Flexibility Week. Students should consult the official UNSW timetable for the exact date.
*   **Support:** Help sessions will run through Flexibility Week. Questions are also welcome on the course forum. A "How to Get Started" video for Assignment 1, recorded by Anna, is available and recommended for students who are struggling to begin.

#### **2. An Introduction to the Python Language**

Python is an exceptionally versatile and widely-used programming language, first developed by Guido van Rossum in 1989. Its utility extends across nearly all domains of computing, making it an essential tool for students in STEM fields, particularly those involving numerical analysis.

##### **2.1. Key Concepts: Why Learn Python?**

*   **Ubiquity and Availability:** Python is available on virtually every general-purpose operating system, including all Unix-like systems. While its memory footprint makes it less common in tiny embedded systems, it is frequently used in more powerful embedded contexts, such as Raspberry Pi devices.
*   **"Batteries Included" Philosophy:** Python comes with an extensive standard library, comprising over 1400 modules, which provides robust support for a vast array of tasks out of the box. This is augmented by the Python Package Index (PyPI), a repository hosting over 600,000 additional packages that can be installed with ease. This ecosystem is arguably the most comprehensive of any programming language, making it highly likely that a library already exists for any given niche task. Its main competitors in this regard are C and JavaScript.
*   **Rapid Prototyping:** Python's concise syntax and high-level abstractions make it possible to develop proof-of-concept prototypes very quickly. It is common practice to prototype a system in Python to validate a design or demonstrate functionality, even if the final implementation must be in a different language (e.g., C for performance reasons). The Python prototype can then serve as a reference implementation during development.
*   **Interactive Calculator:** The Python interpreter can be used as a powerful interactive calculator directly from the command line, which is a convenient tool for quick computations.

**Example: Using Python as a Calculator**
The user can start the Python interpreter and perform calculations directly.
```python
$ python3
Python 3.11.4 (...)
>>> 6 * 7
42
>>> 2**10
1024
```

##### **2.2. The Zen of Python: Language Design Philosophy**

The design of a programming language is a series of philosophical choices made by its creators, which in turn influence how programmers should approach writing code in that language. Python makes its philosophy explicit through a series of aphorisms known as "The Zen of Python", which can be displayed by executing `import this`.

> **Slide Cross-reference:** The full text of "The Zen of Python" is available on Slide 3 of the "Python Introduction" deck.

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Understanding these principles is important for writing idiomatic, or "Pythonic," code. Even if a programmer disagrees with certain choices, adhering to the language's intended style improves readability and maintainability for others familiar with Python. One key principle is "In the face of ambiguity, refuse the temptation to guess." This is reflected in Python's design, which often requires explicit instructions from the programmer where other languages might try to infer intent.

##### **2.3. Strengths and Weaknesses**

*   **Strengths:**
    *   The language facilitates the rapid construction of useful and complex systems.
    *   It excels at prototyping and iterative development.
    *   It possesses an incredibly rich ecosystem of high-level libraries and powerful functional programming features.

*   **Weaknesses:**
    *   **Performance:** Being an interpreted language, Python is generally slower and has higher power consumption than compiled languages like C or Rust. This is often irrelevant for desktop applications but can be a significant factor on mobile devices or in performance-critical systems. For high-performance needs, a language like Rust is a good complement to Python.
    *   **Type Checking:** Static type checking was added to Python as an afterthought. While it is available and extremely valuable for large projects (e.g., millions of lines of code), it is not strictly enforced by the interpreter. For the smaller scripts written in this course, its absence is less critical, but its importance grows with project scale.

##### **2.4. Course Focus: Python as a Scripting Language**

This course will focus on using Python as a scripting language for tasks analogous to those performed with shell scripts, typically involving scripts of 50-100 lines. Consequently, we will not delve into advanced features such as classes, inheritance, and object-oriented design patterns, which are essential for building large-scale applications but are less relevant for the scripting context of this course.

#### **3. Python's Implementation Model: A Spectrum**

Programming languages can be implemented in various ways, typically falling on a spectrum between pure compilation and pure interpretation.

*   **Compilation:** A compiler translates the source code directly into machine code, which is then executed by the CPU. The C language is a classic example of this model.
    **Example: Compiling and Running a C Program**
    ```c
    // hello.c
    #include <stdio.h>
    int main(void) {
        printf("hello, Dylan\n");
        return 0;
    }
    ```
    ```bash
    $ clang hello.c -o hello  # Compilation to machine code
    $ ./hello                 # Execution of machine code
    hello, Dylan
    ```

*   **Interpretation:** An interpreter reads the source code line by line (or statement by statement) and executes the instructions directly. Shell scripting is a prime example.
    **Example: Running a Shell Script**
    ```bash
    # hello.sh
    #!/bin/sh
    echo "hello, Dylan"
    ```
    ```bash
    $ chmod +x hello.sh
    $ ./hello.sh
    hello, Dylan
    ```
    Here, the `sh` program (which is itself machine code) reads and executes the script.

*   **The Reality is a Spectrum:**
    *   While C is typically compiled, C interpreters do exist, though they are uncommon and complex to implement due to features like pointer casting.
    *   Conversely, shell-to-machine-code compilers could exist, but they offer negligible performance benefits and are thus not widely used.
    *   **Python's Position:** Python, like many modern languages (e.g., JavaScript, Java), sits in the middle of this spectrum. The Python interpreter first performs a compilation phase, translating the source code into an intermediate representation called **bytecode**. This bytecode is then executed by a **virtual machine**. This approach combines the platform independence of interpretation with some of the performance benefits of compilation. Advanced implementations, particularly for JavaScript, employ further optimisation techniques like Just-In-Time (JIT) compilation to machine code for performance-critical sections.

> **Slide Cross-reference:** Slides 5 and 6 of the "Python Introduction" deck provide a summary of languages that are typically compiled versus interpreted.

#### **4. The Python Ecosystem: Versions and Libraries**

##### **4.1. Python Versions: A Tale of Two Pythons**

*   **Python 2:** Released in 2000, Python 2 was the standard for many years.
*   **Python 3:** Released in 2008, Python 3 introduced significant, non-backward-compatible changes to the language.
*   **End of Life:** Official support for Python 2 ended in 2020. No new security updates or bug fixes are provided. Despite this, a considerable amount of legacy Python 2 code remains in production systems, and converting it to Python 3 (using tools like `2to3` followed by manual review) is an ongoing task for many organisations.

**Caveat:** The command `python` is ambiguous on many systems. It might invoke Python 2, Python 3, or fail entirely. To ensure predictable behaviour, **always explicitly use `python3`** in your scripts and on the command line.

*   **Python 3 Evolution:** Since its release, Python 3 has evolved with regular minor version updates (e.g., 3.11, 3.12, 3.13). These updates are generally backward-compatible, meaning code written for an older version of Python 3 (e.g., 3.9) will likely run on a newer version (e.g., 3.11). However, breaking changes can occur, particularly regarding library removals or changes in core features like asynchronous functions.

*   **Course Environment:** This course uses **Python 3.11** on the CSE servers. All submitted code must be compatible with this version. While it is unlikely that using a newer version like 3.13 on a personal machine will cause issues for the scope of this course, it is imperative to test all code on the CSE servers before submission.

##### **4.2. Libraries and Modules**

Python's power is significantly amplified by its vast collection of libraries.
*   **Standard Library:** Python includes over 300 standard modules for common tasks (e.g., `math`, `json`, `sys`, `re`). These are accessed using the `import` statement.
*   **Python Package Index (PyPI):** PyPI is a third-party repository containing over 616,000 packages for nearly every conceivable task. These can be easily installed and managed, and we will cover how to do so later in the course.

**Example: Importing and Using a Module**
To access functions for handling JSON data, one can import the `json` module.

```python
import json

# The json module provides functions like json.loads() and json.dumps()
# For example, to load an empty JSON object from /dev/null
# (which represents an empty file)
with open('/dev/null') as f:
    data = json.load(f) # This would raise an error on an empty file, but illustrates the function call
```

#### **5. Executing Python Scripts**

There are several standard ways to run a Python program.

> **Slide Cross-reference:** Slide 9 of the "Python Introduction" deck summarises these methods.

1.  **As a Command-line Argument to the Interpreter:**
    ```bash
    $ python3 my_script.py
    ```
2.  **As an Inline Command (`-c` flag):** This is useful for very short, one-off scripts.
    ```bash
    $ python3 -c 'import sys; print(f"Hello, {sys.platform}")'
    ```
3.  **As an Executable File (using a Shebang):** This is the conventional method for scripts on Unix-like systems. The file must be marked as executable (`chmod +x`), and the first line must be a shebang pointing to the Python interpreter.
    ```python
    # hello.py
    #!/usr/bin/env python3
    print("Hello, world!")
    ```
    ```bash
    $ chmod +x hello.py
    $ ./hello.py
    Hello, world!
    ```

##### **5.1. A Note on Shebangs**

There are two common forms for the Python shebang line:

*   `#!/usr/bin/python3`: This uses a fixed, absolute path to the Python 3 interpreter. It will fail if Python is installed elsewhere.
*   `#!/usr/bin/env python3`: This is generally the preferred method. The `env` program searches the user's `PATH` environment variable to find the `python3` executable. This makes the script more portable, as it will work correctly even if Python is installed in a non-standard location or when using virtual environments. While this distinction is not critical for this course, it is an important piece of practical knowledge.

#### **6. Core Language Features and Syntax**

##### **6.1. Variables and Types**

Python employs a **strong, dynamic type system**.
*   **Strong:** Operations are type-sensitive. You cannot, for instance, add a string to an integer without explicit conversion.
*   **Dynamic:** Types are checked at runtime, not compile time. A single variable name can refer to values of different types at different points in the program.
*   **Type Association:** Types are associated with **values**, not variables. A variable is merely a name that refers to a value (object).

**Example: Dynamic Typing**
```python
>>> x = 42
>>> type(x)
<class 'int'>

>>> x = "Hello"
>>> type(x)
<class 'str'>
```

*   **Key Built-in Types:**
    *   `int`: Arbitrary-precision integers. There is no fixed bit limit; Python allocates as much memory as needed.
    *   `float`: 64-bit IEEE 754 floating-point numbers (equivalent to a `double` in C).
    *   `str`: Immutable sequences of Unicode characters (strings).
    *   `list`: Mutable, ordered sequences of objects.
    *   `tuple`: Immutable, ordered sequences of objects.
    *   `dict`: Mappings of keys to values (hash maps).
    *   `bool`: `True` or `False`.
    *   `NoneType`: The type of the special value `None`, used to represent the absence of a value.

##### **6.2. Operators**

Python's operator set will be largely familiar to C programmers, with some key differences.

> **Slide Cross-reference:** Slides 12-18 of the "Python Introduction" deck provide comprehensive tables of these operators.

*   **Comparison (`==`, `!=`, `>`, `<`, `>=`, `<=`):** These behave as in C.
    *   **Caveat:** Python allows comparisons between objects of different types (e.g., `5 == "5"`). This expression is valid and evaluates to `False`, whereas in C it would cause a compilation error. This can introduce subtle bugs if a programmer is not mindful of the types of their variables.
*   **Arithmetic (`+`, `-`, `*`, `%`):**
    *   `**`: Exponentiation (e.g., `2**3` is 8).
    *   `/`: Floating-point division (e.g., `5 / 2` is `2.5`).
    *   `//`: Integer division (e.g., `5 // 2` is `2`).
*   **Logical (`and`, `or`, `not`):** Python uses words instead of C's symbols (`&&`, `||`, `!`).
*   **Identity (`is`, `is not`):** These operators test if two names refer to the exact same object in memory, not just if they have the same value.
*   **Membership (`in`, `not in`):** These test for the presence of a value within a sequence (like a list or string).
*   **Missing Operators:** Python does **not** have the increment (`++`) or decrement (`--`) operators. Use the compound assignment forms `x += 1` and `x -= 1` instead.
*   **Walrus Operator (`:=`):** A recent addition, the assignment expression operator allows a value to be assigned to a variable as part of a larger expression.

##### **6.3. The Concept of "Truthiness"**

In boolean contexts (like an `if` statement), Python evaluates various values as either `True` or `False`.

> **Slide Cross-reference:** A detailed list is on Slide 20 of the "Python Introduction" deck.

*   **Values that are `False`:**
    *   The boolean constant `False`.
    *   The special value `None`.
    *   Any numeric zero (`0`, `0.0`, `0j`).
    *   Any empty sequence or collection (e.g., an empty string `""`, an empty list `[]`, an empty tuple `()`, an empty dictionary `{}`).
*   **Values that are `True`:**
    *   Everything else. This includes non-empty strings (even `"0"` or `"False"`), non-zero numbers, and non-empty collections.

##### **6.4. Control Structures**

*   **Syntax:** Python uses **indentation** to define code blocks, not curly braces (`{}`) as in C. A colon (`:`) is used to introduce a new block (e.g., after `if`, `while`, `for`, `def`). Statements are typically separated by newlines; semicolons are allowed but highly discouraged in normal code.

*   **Selection (`if`/`elif`/`else`):**
    ```python
    if x > 10:
        print("x is large")
    elif x > 5:
        print("x is medium")
    else:
        print("x is small")
    ```

*   **Iteration (`while` and `for`):**
    *   `while`: Executes a block as long as a condition is true.
        ```python
        i = 0
        while i < 5:
            print(i)
            i += 1
        ```
    *   `for`: Iterates over the items of any sequence or iterable object. This is more akin to a shell `for` loop or a C++ range-based `for` loop than a traditional C `for` loop.
        ```python
        for fruit in ["apple", "banana", "cherry"]:
            print(fruit)
        ```
    *   **The `range()` function:** To create C-style loops that iterate a specific number of times, the `range()` function is used. `range(stop)` goes from 0 up to (but not including) `stop`. `range(start, stop, step)` provides more control.
        ```python
        # Equivalent to: for (int i = 0; i < 10; i++)
        for i in range(10):
            print(i)
        ```

*   **Loop Control:**
    *   `break`: Exits the innermost enclosing loop immediately.
    *   `continue`: Skips the rest of the current iteration and proceeds to the next one.
    *   **Loop `else` clause:** A `for` or `while` loop can have an optional `else` block. This block is executed only if the loop terminates normally (i.e., not by a `break` statement). This is a unique feature of Python.

##### **6.5. Exception Handling with `try`/`except`**

When an error occurs during execution, Python raises an **exception**. If unhandled, this terminates the program. The `try...except` block allows you to intercept and handle these exceptions gracefully.

*   The code that might raise an exception is placed in the `try` block.
*   Code to handle a specific type of exception is placed in a corresponding `except` block.

**Example: Handling `ValueError` during Type Conversion**
When converting user input to an integer, the `int()` function will raise a `ValueError` if the input string is not a valid integer.

```python
line = input("Enter a number: ")
try:
    number = int(line)
    print(f"You entered {number}")
except ValueError:
    print(f"Error: '{line}' is not a valid integer.")
```
This is the Pythonic way to handle potential errors, often referred to as "It's Easier to Ask for Forgiveness than Permission" (EAFP), in contrast to checking conditions beforehand ("Look Before You Leap" - LBYL). For instance, it is generally better to attempt a conversion and catch the exception than to try to validate the string with a regular expression first.

***

This concludes the introductory overview. The following sections will delve into more specific features, including sequence types, file I/O, external programs, web interaction, and functions, illustrated with complete script examples.