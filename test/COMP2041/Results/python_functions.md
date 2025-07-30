Based on the provided lecture transcript and slides, the following comprehensive lecture notes have been prepared.

### **Introduction and Course Administration**

The lecture begins with administrative updates concerning course assignments. Assignment Two, which will focus on Python, is scheduled for release. A significant portion of the marking for Assignment One (80%) is based on automated tests. Students are advised to review their draft marks and report any potential discrepancies in the marking process via the class forum. Tutors will conduct hand-marking to assess submissions that, despite showing progress, did not pass automated tests, or for cases where last-minute errors (e.g., syntax errors) caused a student's code to fail all tests despite being largely complete.

---

### **The `subprocess` Module: Interfacing with External Programs**

This section explores the `subprocess` module, which provides the capability to execute external programs from within a Python script. This functionality is analogous to running commands in a shell script, but with programmatic control available in Python.

#### **Key Concepts**

The primary function for this purpose is `subprocess.run()`. It executes a command and returns a `CompletedProcess` object, which contains information about the execution, such as the command's return code and its standard output and error streams.

By default, the standard input, output, and error streams of the subprocess are inherited from the parent Python process. However, it is frequently desirable to capture the output of the command for further processing within the Python program. This can be achieved using the `capture_output=True` argument.

A critical detail when capturing output is the distinction between binary and text data. By default, `subprocess` captures output as a binary byte string. To capture it as a regular text string (UTF-8 decoded), the argument `text=True` must be specified. This is a common requirement and a frequent source of programming errors. In older codebases, a similar effect was achieved using the `universal_newlines=True` argument, which is now superseded by `text=True`.

#### **Examples**

**1. Basic Execution and Return Code**

To run the `date` command with the `--utc` flag, one can use the following code. The command and its arguments are passed as a list.

```python
import subprocess
# Executes 'date --utc'
p = subprocess.run(['date', '--utc'])
# The CompletedProcess object contains the return code
print(p.returncode) # Will be 0 on success
```

If an invalid option is provided, the command will fail, and the `returncode` will be a non-zero value, typically 1, which can be checked programmatically to alter the script's behaviour.

```python
# 'cat' is not a valid option for the date command
p_fail = subprocess.run(['date', '--cat'])
print(p_fail.returncode) # Will be 1
```

**2. Capturing and Processing Output**

To capture the output of the `date` command and extract a specific piece of information, such as the month, the following approach can be used.

```python
import subprocess
# Note the use of capture_output=True and text=True
p = subprocess.run(['date', '--utc'], capture_output=True, text=True)

# The captured output is in p.stdout
output_string = p.stdout
# Example of processing the string to extract the month
month = output_string.strip().split()[1]
print(month)
```
Similarly, standard error can be captured via the `p.stderr` attribute if `capture_output=True` is set.

**3. Supplying Input to a Program**

The `subprocess.run()` function can also send data to the standard input of the program being executed using the `input` argument. The following example demonstrates running the `tr` command to convert an uppercase string to lowercase.

```python
import subprocess

message = "HELLO WORLD"
# The 'input' argument sends data to the program's stdin
# text=True is used for both input and output
p = subprocess.run(['tr', 'A-Z', 'a-z'], input=message, text=True, capture_output=True)

# The transformed string is in p.stdout
print(p.stdout) # prints "hello world\n"
```

#### **Caveats and Security Considerations**

While `subprocess` is powerful, its use should be judicious.

*   **Prefer Internal Modules:** For many common tasks, such as obtaining the current date or performing string manipulations, Python has built-in modules (e.g., `datetime`, string methods like `.lower()`). These internal solutions are almost always more robust, secure, and significantly faster than running an external program. The example of using `tr` to lowercase a string is illustrative; the Python string method `message.lower()` is vastly more efficient.

*   **The Danger of `shell=True`:** The `subprocess.run()` function has a `shell=True` argument that allows a raw command string, including shell pipelines and metacharacters, to be executed. While convenient, this is an **extremely dangerous practice** if any part of the command string is derived from external or user-supplied input.

    An attacker can inject malicious commands via shell metacharacters (e.g., `;`, `|`, `$()`). This is a common and severe security vulnerability known as Shell Injection.

    **Example of Vulnerable Code:**
    ```python
    # DANGEROUS: Do not do this with untrusted input
    email_address = get_user_input()
    # If email_address is "a@b.com; rm -rf /", a malicious command is run
    subprocess.run(f"mail -s 'Welcome' {email_address}", shell=True)
    ```

    Attempting to mitigate this by quoting the input is futile, as an attacker can simply include quotes in their malicious payload. Even seemingly safe commands like `ls *` can be vulnerable if an attacker can create files with malicious names (e.g., a filename starting with `-` or containing command substitutions) in the target directory.

    **Recommendation:** Avoid `shell=True` unless you have absolute control over the entire command string and there is no possibility of external data influencing its content.

---

### **Python and the Web**

This section details methods for interacting with web resources using Python, from serving content to fetching and parsing it.

#### **Key Concepts**

**1. Running a Simple Web Server**

Python's standard library includes a simple HTTP server module, which is invaluable for development and testing. It can be run directly from the command line to serve files from the current directory.

**Example:**
To start a web server on port 8080, execute the following command in the desired directory:
```bash
python3 -m http.server 8080
```
This server can then be accessed by web browsers or command-line tools like `curl`.

**2. Fetching Web Content**

To programmatically retrieve data from a URL, Python provides the `urllib.request` module. The primary function is `urllib.request.urlopen()`, which opens a network connection to a URL and returns a response object. The content can then be read from this object.

**Example:**
```python
import urllib.request

# The URL to fetch
url = 'http://localhost:8080/hello.txt'

# Make the request and get the response object
response = urllib.request.urlopen(url)

# Read the content from the response
web_page_content = response.read()

# The content is often bytes and may need decoding
print(web_page_content.decode('utf-8'))
```
*Note: While `urllib` is built-in, the third-party `requests` library is extremely popular and often considered more user-friendly for complex tasks. It was noted that `requests` averages 20 million downloads a day, underscoring its prevalence.*

**3. Parsing HTML with Beautiful Soup**

Web pages are typically structured with HTML. While simple data might be extracted with regular expressions, this approach is brittle and fails with complex or changing HTML. A robust solution is to use a dedicated HTML parsing library. **Beautiful Soup** is a widely used Python library for this purpose. It parses an HTML document into a tree of Python objects that can be easily navigated and queried.

**Example:**
The following code fetches the UNSW homepage and uses Beautiful Soup to extract only the visible text, filtering out content from tags like `<script>` and `<style>`.

```python
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.unsw.edu.au'
response = urllib.request.urlopen(url)
web_page = response.read()

# Create a BeautifulSoup object using the 'html5lib' parser
soup = BeautifulSoup(web_page, 'html5lib')

# Define tags whose text content should be ignored
tags_to_ignore = {'script', 'style'}

# Iterate through all text nodes in the document
for element in soup.find_all(text=True):
    # If the text is not inside an ignored tag...
    if element.parent.name not in tags_to_ignore:
        text = element.get_text(strip=True)
        if text:
            print(text)
```
This demonstrates the power of using a proper parser to treat a web page as a structured document rather than a raw string.

#### **Real-World Application: The UNSW Handbook Proxy**

A case study was presented involving the UNSW Handbook website. A previous year's lab exercise caused a large number of students to make many requests to the Handbook, leading the site administrators to implement rate-limiting, which broke the lab.

The solution, developed rapidly by a course administrator, was a **proxy server**. This server sits between the students' scripts and the real Handbook website.
*   When a student script requests a page for the first time, the proxy fetches it from the Handbook, stores a copy (caching), and serves it to the student.
*   For all subsequent requests for that same page, the proxy serves the cached copy directly, without contacting the Handbook.

This system, built with Python using the **Flask** web framework and **Redis** for caching, dramatically reduced the load on the Handbook server. It also abstracted away complexities like **pagination** (where a large result set is split across multiple pages), making the students' task simpler. This example serves as a powerful motivator, illustrating how Python can be used to quickly build robust, real-world solutions.

---

### **Python Functions**

This section provides an in-depth exploration of Python functions, covering their definition, argument handling, scope rules, and common pitfalls.

#### **Defining Functions and Handling Arguments**

**1. Basic Definition and Argument Types**
Functions are defined with the `def` keyword. They can be called with positional arguments, where order matters, or keyword arguments, where order does not. Keyword arguments must follow any positional arguments in a function call.

*   **Slide Cross-reference:** Slide 2

**Example:**
```python
def polly(x, a, b, c):
    return a * x ** 2 + b * x + c

# Positional arguments
polly(3, 5, -3, 6) # returns 42

# Keyword arguments
polly(a=5, c=6, b=-3, x=3) # returns 42

# Mixed arguments
polly(3, c=6, b=-3, a=5) # returns 42
```

**2. Default Argument Values**
Parameters can be given default values, making them optional during a function call. This is highly beneficial for maintaining clean function interfaces and for adding new parameters to existing functions without breaking old code.

*   **Slide Cross-reference:** Slide 3

**Example:**
```python
def polly(x, a=1, b=2, c=0):
    return a * x ** 2 + b * x + c

polly(3) # a=1, b=2, c=0 are used. Returns 15.
polly(x=1, b=1) # a=1, c=0 are used. Returns 2.
```

**3. Variable Numbers of Arguments (`*args`, `**kwargs`)**
Python allows functions to accept an arbitrary number of arguments using the `*` and `**` operators.
*   `*args`: Packs all extra positional arguments into a tuple.
*   `**kwargs`: Packs all extra keyword arguments into a dictionary.

Conversely, these operators can be used when *calling* a function to unpack an iterable or a dictionary into arguments.

*   **Slide Cross-reference:** Slides 7, 8

**Examples:**
```python
# Function Definition (Packing)
def f(*args, **kwargs):
    print('positional arguments:', args)
    print('keywords arguments:', kwargs)

f("COMP", 2041, answer=42)
# prints:
# positional arguments: ('COMP', 2041)
# keywords arguments: {'answer': 42}

# Function Call (Unpacking)
arguments = ['Hello', 'there']
keyword_args = {'end': '!!!\n', 'sep': ' --- '}
print(*arguments, **keyword_args)
# prints: Hello --- there!!!
```

#### **Caveats and Common Pitfalls**

**1. Mutable Default Argument Values**
This is a critical and common pitfall in Python. A default argument value is created **only once**, when the function is defined. If that default value is a mutable object (like a list or dictionary), all calls to the function that rely on the default will share and modify the *same object*.

*   **Slide Cross-reference:** Slide 4

**Example of the Bug:**
```python
def append_one(x = []):
    x.append(1)
    return x

print(append_one()) # prints [1]
print(append_one()) # prints [1, 1] -- Unexpected!
print(append_one()) # prints [1, 1, 1] -- The same list is being modified.
```
This occurs because the `[]` is created once, and the name `x` inside the function refers to this single list object across multiple calls.

**The Workaround:**
The standard practice is to use an immutable value like `None` as the default and then create a new mutable object inside the function if the argument was not provided.

*   **Slide Cross-reference:** Slide 5
```python
def append_one(x = None):
    if x is None:
        x = [] # A new list is created for each call
    x.append(1)
    return x

print(append_one()) # prints [1]
print(append_one()) # prints [1]
```
**Guideline:** Do not use mutable objects (lists, dictionaries, sets) as default values for function parameters.

**2. Object Identity vs. Equality**
The `is` operator checks for object identity (whether two names refer to the exact same object in memory), while the `==` operator checks for equality (whether two objects have the same value). Understanding this distinction is key to understanding the mutable default argument issue. The `id()` function returns a unique identifier for an object, which is often its memory address.

**3. Variable Scope**
*   A variable that is assigned a value anywhere inside a function is, by default, **local** to that function.
*   A variable that is read from but never assigned to within a function is treated as **global**.
*   The `global` keyword can be used to explicitly declare that an assignment within a function should modify a global variable.

*   **Slide Cross-reference:** Slides 11, 12, 13

**Example:**
```python
x = 12
def f():
    x = 34 # Creates a new local variable 'x'
    print(x) # prints 34

def g():
    global x # Refers to the global 'x'
    x = 56 # Modifies the global 'x'
    print(x) # prints 56

f()
print(x) # prints 12 (global x is unchanged)

g()
print(x) # prints 56 (global x has been changed)
```
Global variables can make code difficult to reason about, as their values can be changed by any function that declares them global. They are generally avoided, except for defining module-level constants.

#### **Standard Idioms and Conventions**

**1. The `__main__` Idiom**
Python does not have a special `main` function like C. To allow a file to be both runnable as a script and importable as a module, the following idiom is used. The special variable `__name__` is set to the string `'__main__'` when a file is executed directly.

*   **Slide Cross-reference:** Slide 9
```python
def main_logic():
    print("This is the main logic.")

if __name__ == '__main__':
    main_logic()
```

**2. Docstrings**
A string literal placed as the very first statement in a function definition serves as its documentation string, or **docstring**. These are accessible via the function's `__doc__` attribute and are used by tools like `help()`, IDEs, and automatic documentation generators.

*   **Slide Cross-reference:** Slide 10
```python
def polly(x, a, b, c):
    """
    Calculates the value of a quadratic polynomial.

    Args:
        x: The independent variable.
        a: The coefficient of the squared term.
        b: The coefficient of the linear term.
        c: The constant offset.

    Returns:
        The value of the polynomial at x.
    """
    return a * x ** 2 + b * x + c

help(polly) # This will display the docstring.
```

---

### **Higher-Order Programming, List Comprehensions, and Lambdas**

This section covers functional programming concepts in Python, providing concise and powerful ways to work with sequences of data.

#### **List Comprehensions**

A list comprehension provides a concise syntax for creating a list based on an existing iterable. They are often more readable and efficient than explicit `for` loops.

*   **Syntax:** `[expression for item in iterable if condition]`
*   **Slide Cross-reference:** Slide 14

**Examples:**
```python
# Create a list of the first 10 cubes
cubes = [x**3 for x in range(10)]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Create a list of the cubes of odd numbers under 10
odd_cubes = [x**3 for x in range(10) if x % 2 == 1]
# [1, 27, 125, 343, 729]
```

#### **Lambda Functions**

The `lambda` keyword creates a small, anonymous function. It is restricted to a single expression and is most useful when a simple function is needed as an argument to a higher-order function (like `map` or `filter`).

*   **Syntax:** `lambda arguments: expression`
*   **Slide Cross-reference:** Slide 15

**Caveat: Variable Binding**
A `lambda` function's variables are bound at the time the lambda is *evaluated*, not when it is defined. This can lead to unexpected behaviour.

*   **Slide Cross-reference:** Slide 16
```python
answer = 42
f = lambda x: x + answer
answer = 15
f(10) # returns 25 (uses answer=15), not 52 (answer=42)
```

#### **Built-in Higher-Order Functions**

Python includes several powerful built-in functions for working with iterables.

1.  **`enumerate(iterable, start=0)`**: Returns an iterator of tuples, each containing a count (starting from `start`) and a value from the iterable. Useful for loops where both the index and the value are needed.
    *   **Slide Cross-reference:** Slide 17

2.  **`zip(*iterables)`**: Returns an iterator of tuples, where the *i*-th tuple contains the *i*-th element from each of the input iterables. The iteration stops when the shortest input iterable is exhausted.
    *   **Slide Cross-reference:** Slide 18

3.  **`map(function, iterable, ...)`**: Applies `function` to every item of `iterable` and returns an iterator of the results.
    *   **Slide Cross-reference:** Slide 21

4.  **`filter(function, iterable)`**: Returns an iterator of items from `iterable` for which `function` returns `True`.
    *   **Slide Cross-reference:** Slide 23

#### **Synthesis Example: Dot Product**

The calculation of a dot product was used to showcase different programming styles, moving from an imperative C-like style to a more functional and Pythonic style.

Let `a = [1, 2, 3]` and `b = [4, 5, 6]`.

1.  **C-style `for` loop with index:**
    ```python
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    ```

2.  **Pythonic `for` loop with `zip`:** (Considered highly readable)
    ```python
    total = 0
    for x, y in zip(a, b):
        total += x * y
    ```

3.  **List Comprehension with `sum`:** (Very common and Pythonic)
    ```python
    total = sum([x * y for x, y in zip(a, b)])
    ```

4.  **`map` with `lambda` and `sum`:** (A functional approach)
    ```python
    total = sum(map(lambda x, y: x * y, a, b))
    ```

This example illustrates that there are often multiple ways to achieve the same result in Python, with trade-offs in readability and programming style. The use of `zip` and list comprehensions is often a good balance of conciseness and clarity.

#### **Advanced Topics (Mentioned for Further Study)**

*   **Generators:** Functions that use the `yield` keyword to produce a sequence of values lazily, one at a time. They are memory-efficient for very large or infinite sequences.
*   **Decorators:** A specialized type of higher-order function used to modify or enhance other functions or methods. They are a powerful tool for meta-programming.