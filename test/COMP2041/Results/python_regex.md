Here are the comprehensive lecture notes for COMP(2041/9044) Lectures 11 and 12, meticulously compiled from the provided transcript and slides.

***

### **Lecture Notes: Python File I/O, Dictionaries, and Regular Expressions**

These notes cover the content from Lectures 11 and 12, focusing on Python as a scripting language. The topics include a review of Python sequences, an in-depth look at file input/output, the use of dictionaries for data aggregation, and a comprehensive introduction to Python's powerful regular expression capabilities.

### **1. Course Administration**

*   **Assignment 1**: Was due at noon on the day of Lecture 11. Students are strongly encouraged to submit their work even if incomplete, as the marking scheme is designed to award partial marks.
*   **Late Penalties**: The standard UNSW late penalty applies, which is a 5% reduction in the maximum achievable mark per day, for up to five days. This is calculated on an hourly basis, equating to a 0.2% reduction per hour.
*   **Lab 5**: Was also due at noon on the day of Lecture 11.
*   **Weekly Tests**: The tests for Week 5 and Week 6 were both due on the Thursday of Week 7.
*   **Assignment 2**: This will be a Python-based assignment, expected to be released early in Week 8 and due at 9 a.m. on the Monday of Week 11.
*   **Final Exam**:
    *   The provisional timetable is out and is unlikely to change.
    *   The exam is scheduled for a full day, but it is a three-hour exam. There will be a morning and an afternoon session.
    *   Students will be able to indicate their preferred session. The exams team will attempt to accommodate preferences.
    *   Students with known exam clashes will be automatically allocated to the non-clashing session.
    *   Students with special exam conditions (EAS) will have them applied automatically. Confirmation will be sent closer to the exam date.
    *   Questions regarding the exam should be directed to the course forum or asked during the final lecture in Week 10 to ensure all students have access to the same information.

### **2. Recap of Python Sequences and Basic Operations**

This section revisits fundamental Python concepts, particularly those relevant to scripting tasks.

#### **Key Concepts**

*   **Sequence Types**: Python provides three primary sequence types:
    1.  **Lists**: Mutable (changeable) collections, heavily used in Python programming.
    2.  **Tuples**: Immutable (fixed) collections. Their immutability is crucial in contexts where a constant value is required, such as dictionary keys.
    3.  **Ranges**: A sequence type that generates a sequence of integers, typically used to control `for` loops.
*   **Mutability**: The key distinction between lists and tuples. Lists are mutable, meaning their contents can be altered after creation. Tuples are immutable; once created, they cannot be changed.
*   **Slices**: A powerful feature for extracting sub-sequences from any sequence type. The syntax `sequence[start:end]` creates a new sequence. A common and useful trick is `sys.argv[1:]`, which creates a new list containing all command-line arguments except for the program name itself. Mastery of slices is essential for efficient Python programming.
*   **Exception Handling**: Python uses exceptions to signal abnormal conditions. Instead of returning a special error value, a function will "throw" an exception. If unhandled, this terminates the program.
    *   **The EAFP Philosophy**: A core Python coding philosophy is "It's Easier to Ask for Forgiveness than Permission" (EAFP). Rather than pre-emptively checking if an operation is valid (e.g., validating that a string contains only digits before converting it to an integer), the preferred approach is to `try` the operation and `except` any exceptions that arise. This often leads to cleaner and more robust code.

#### **Example: Summing Command-Line Arguments**

This example demonstrates processing command-line arguments, using slices, type conversion, and exception handling.

```python
import sys

total = 0
# sys.argv is a list of command-line arguments.
# The first element, sys.argv[0], is the program name.
# The slice [1:] creates a new list without the program name.
for arg in sys.argv[1:]:
    try:
        # Command-line arguments are strings; they must be converted.
        total += int(arg)
    except ValueError:
        # This block executes if int(arg) fails.
        print(f"Error: Non-integer argument '{arg}' ignored.", file=sys.stderr)

print(total)
```

### **3. Python File Input/Output (I/O)**

This section covers the mechanisms for reading from and writing to files in Python.

#### **Key Concepts**

*   **Standard Streams**: The `sys` module provides access to standard input (`sys.stdin`), standard output (`sys.stdout`), and standard error (`sys.stderr`).
*   **Iterating over Standard Input**: `sys.stdin` can be treated as an iterator that yields one line at a time. This allows for the elegant and memory-efficient construct `for line in sys.stdin:`.
*   **The `open()` Function**: Used to open a file and obtain a file object. Its basic syntax is `open(filename, mode)`.
    *   **Modes**: The second argument specifies the mode. Common modes include:
        *   `'r'`: Read (default).
        *   `'w'`: Write (creates a new file or truncates an existing one).
        *   `'a'`: Append (adds to the end of an existing file).
    *   **Text vs. Binary**: By default, files are opened in text mode, assuming a default encoding (often UTF-8). To handle raw bytes, a 'b' must be appended to the mode (e.g., `'rb'`, `'wb'`).
*   **The `with` Statement (Context Manager)**: This is the **strongly recommended** pattern for file I/O. It ensures that the file's `close()` method is automatically called when the block is exited, regardless of how it is exited (normally or via an exception).
*   **File Object Methods**:
    *   `.read()`: Reads the entire file into a single string.
    *   `.readlines()`: Reads the entire file into a list of strings, where each string is a line.
    *   `.write(string)`: Writes a single string to the file.
    *   `.writelines(list_of_strings)`: Writes all strings from a list to the file.
*   **Handling I/O Errors**: Operations that interact with the operating system, such as opening a file, can fail for various reasons (e.g., file not found, permission denied). These failures raise an `OSError` exception (or one of its subclasses like `FileNotFoundError`).

#### **Caveats**

*   **Closing Files**: It is crucial to close files, especially when writing. The operating system buffers output, and `close()` ensures that all buffered data is written to the disk. While forgetting to close a read-only file is less critical, it can still lead to resource leaks (exceeding the maximum number of open files) in long-running programs. The `with` statement handles this automatically.
*   **Reading Large Files**: Using `.read()` or `.readlines()` on very large files (e.g., gigabytes) can consume an excessive amount of memory. In such cases, iterating over the file object line-by-line (`for line in f:`) is the preferred, memory-efficient approach.

#### **Example: A File Copy Utility (`cp`)**

The following examples demonstrate building a file copy utility, progressively refining the code to be more robust and Pythonic.

**Version 1: Explicit `close()` calls (Not Recommended)**
```python
# This version is functional but less robust.
# It does not use the recommended 'with' statement.
import sys

# Assume sys.argv[1] is source, sys.argv[2] is destination
in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

for line in in_file:
    out_file.write(line)

in_file.close()
out_file.close()
```

**Version 2: The Recommended `with` Statement and Error Handling**
```python
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} source_file destination_file", file=sys.stderr)
    sys.exit(1)

try:
    # 'with' ensures files are closed automatically.
    # Nesting 'with' statements is common.
    with open(sys.argv[1], 'r', encoding='utf-8') as in_file:
        with open(sys.argv[2], 'w', encoding='utf-8') as out_file:
            for line in in_file:
                out_file.write(line)
except OSError as e:
    # Catch any OS-level error during file operations.
    print(f"{sys.argv[0]}: Error: {e}", file=sys.stderr)
    sys.exit(1)
```

#### **Life Advice: Use Existing Libraries**

Before writing code for a common task, one should check if a standard library already provides a solution. This saves time, leverages expert-written and well-tested code, and reduces the likelihood of bugs.

**Example: File Copying with `shutil`**
```python
import sys
import shutil

# try/except block for error handling is still needed
try:
    shutil.copy(sys.argv[1], sys.argv[2])
except (OSError, shutil.SameFileError) as e:
    print(f"{sys.argv[0]}: Error: {e}", file=sys.stderr)
    sys.exit(1)
```
*Caveat*: The `shutil.copy` function copies file contents but not all metadata by default. `shutil.copy2` attempts to copy metadata as well.

#### **The `subprocess` and `fileinput` Modules**

*   **`subprocess`**: This module allows a Python script to run external programs. For example, `subprocess.run(['cp', 'source', 'dest'])` would execute the system's `cp` command. While powerful, this is often disallowed in course exercises that are intended to test Python proficiency, not shell scripting via a Python wrapper.
*   **`fileinput`**: This convenient module provides a loop that transparently iterates over lines from files listed on the command line, or from standard input if no files are provided. This perfectly mimics the behavior of standard Unix filters like `cat`, `grep`, and `sed`.

### **4. Python Dictionaries (`dict`)**

Dictionaries are a fundamental Python data structure for storing key-value pairs.

#### **Key Concepts**

*   **Associative Arrays**: Dictionaries are also known as associative arrays, hash maps, or maps. They map a *key* to a *value*.
*   **Keys**: Dictionary keys must be of an **immutable** type. This commonly includes strings, numbers, and tuples. Lists cannot be used as keys because they are mutable.
*   **Core Operations**:
    *   Creation: `my_dict = {}` or `my_dict = {'key1': 'value1'}`.
    *   Accessing: `value = my_dict['key']`. This will raise a `KeyError` if the key does not exist.
    *   Adding/Updating: `my_dict['new_key'] = 'new_value'`. This creates the entry if the key is new or updates the value if the key already exists.
    *   Checking for Existence: The `in` operator (`if key in my_dict:`) is the canonical way to check if a key is present.
*   **Safe Access with `.get()`**: The `my_dict.get(key, default)` method provides safe access. It returns the value for `key` if it exists, otherwise it returns `default`. If `default` is not specified, it defaults to `None`. This avoids `KeyError` exceptions.
*   **Iteration**:
    *   `for key in my_dict:` iterates over the keys.
    *   `my_dict.items()` returns a view object of `(key, value)` tuples, which is useful for iterating over both simultaneously: `for key, value in my_dict.items():`.

#### **Example: Counting Enrollments**

This comprehensive example reads course codes and enrollment data to produce a summary report. It demonstrates dictionary creation, population, and safe access.

```python
import collections

# Step 1: Read course codes into a dictionary for easy lookup.
course_names = {}
# Assumes course_codes.tsv is a tab-separated file: <code>\t<name>
with open("course_codes.tsv", "r", encoding="utf-8") as f:
    for line in f:
        # Using string split is often simpler and faster than regex for fixed delimiters.
        course_code, course_name = line.strip().split("\t", maxsplit=1)
        course_names[course_code] = course_name

# Step 2: Count enrollments using a dictionary.
enrollments_count = {}
# Assumes enrollments.tsv is a pipe-separated file: <code>|<zid>|<name>...
with open("enrollments.tsv", "r", encoding="utf-8") as f:
    for line in f:
        course_code = line.split("|")[0]
        # Common pattern: initialize if key is new, then increment.
        if course_code not in enrollments_count:
            enrollments_count[course_code] = 0
        enrollments_count[course_code] += 1

# Step 3: Print a sorted, formatted report.
# .items() gives (key, value) pairs. sorted() sorts them by key.
for course_code, enrollment in sorted(enrollments_count.items()):
    # Use .get() to provide a default value for courses not in our name list.
    name = course_names.get(course_code, "???")
    print(f"{enrollment:4} {course_code} {name}")
```

#### **Related Data Types: `set` and `collections.Counter`**

*   **`set`**: An unordered collection of unique, immutable elements. Sets are highly optimized for membership testing (`in`). They are the ideal tool when you only need to track which items have been seen, without an associated value.
*   **`collections.Counter`**: A dictionary subclass specialized for counting. It simplifies the counting pattern: you can increment a key's count without first checking if it exists (it defaults to 0).
*   **`collections.defaultdict`**: A dictionary subclass that allows one to specify a "factory" function (e.g., `int`, `list`, `dict`) which is called to provide a default value for a non-existent key. `defaultdict(int)` behaves similarly to a `Counter`. `defaultdict(list)` is useful for grouping items into lists.

### **5. Python Regular Expressions (`re` module)**

Python's `re` module provides an implementation of regular expressions with a syntax and feature set largely compatible with the influential Perl Compatible Regular Expressions (PCRE) library.

#### **Slide Cross-Reference**: Slides 2-27 cover this topic in detail.

#### **Historical Context**

The regexes used in Python are more powerful than the POSIX Extended Regular Expressions found in tools like `grep -E`. They descend from Henry Spencer's C library, which was significantly extended by Larry Wall for the Perl language, creating the PCRE standard. Python's `re` module adopted most of these powerful features.

#### **Core Functions**

*   `re.search(regex, string)`: Scans through a `string` looking for the **first location** where the `regex` produces a match. Returns a match object on success, `None` on failure.
*   `re.match(regex, string)`: Only attempts to match the `regex` at the **beginning** of the `string`. Equivalent to `re.search('^' + regex, string)`.
*   `re.fullmatch(regex, string)`: Only succeeds if the `regex` matches the **entire** `string`. Equivalent to `re.search('^' + regex + '$', string)`.
*   `re.sub(regex, replacement, string)`: Returns a new string obtained by replacing all occurrences of `regex` in `string` with `replacement`.
*   `re.findall(regex, string)`: Returns a **list of all non-overlapping matches** of `regex` in `string`. This function is often an underused but powerful tool that can simplify complex parsing tasks.
*   `re.split(regex, string)`: Splits `string` by the occurrences of `regex`, returning a list of substrings. This is a more powerful version of the string `.split()` method.

#### **Enhanced Syntax and Features**

*   **Raw Strings**: Prefixing a string with `r` (e.g., `r'\d+'`) creates a raw string where backslashes are treated as literal characters. This is highly recommended for writing regular expressions to avoid confusion with Python's own escape sequences (e.g., `\n`) and to prevent "leaning toothpick syndrome" (`'\\d+'`).
*   **Character Classes**:
    *   `\d`: Any digit. (`\D` for non-digit).
    *   `\w`: Any "word" character (alphanumeric plus underscore). (`\W` for non-word).
    *   `\s`: Any whitespace character (space, tab, newline, etc.). (`\S` for non-whitespace).
*   **Anchors and Boundaries**:
    *   `\b`: A zero-width assertion that matches at a word boundary (e.g., between a `\w` and a `\W`, or at the start/end of the string). This is extremely useful for matching whole words, e.g., `r'\bcat\b'` will match `'cat'` but not `'caterpillar'`. (`\B` matches where there is no word boundary).
    *   `\A` and `\Z`: Match the start and end of the string, respectively. Similar to `^` and `$`.
*   **Capturing and Match Objects**:
    *   Parentheses `()` in a regex serve two purposes: grouping parts of the pattern and **capturing** the substring that matches the enclosed part.
    *   The match object returned by `re.search` contains information about the match.
        *   `m.group(0)` or `m.group()`: Returns the entire matched string.
        *   `m.group(n)`: Returns the string captured by the *n*-th set of parentheses.
        *   `m.groups()`: Returns a tuple of all captured strings.
    *   Captured groups can be referenced in the replacement string of `re.sub` using `\1`, `\2`, etc.
*   **Back-references**: A captured group can be referenced *within the regex itself* using `\1`. For example, `r'(\w+)\s+\1'` matches a word repeated twice. This feature significantly increases the power of the regex engine but also its computational complexity, making matching potentially NP-hard.
*   **Non-Capturing Groups**: `(?:...)` groups a part of a pattern without capturing it. This is useful when you need parentheses for grouping but do not want to create a numbered capture group.

#### **Greedy vs. Non-Greedy Matching**

*   **Greedy**: By default, quantifiers like `*`, `+`, and `?` are *greedy*. They match as **much text as possible**. For example, in the string `"abbbc"`, `r'ab+'` will match `"abbb"`.
*   **Non-Greedy (or Reluctant)**: Appending a `?` to a quantifier (`*?`, `+?`, `??`) makes it *non-greedy*. It will match as **little text as possible**. In `"abbbc"`, `r'ab+?'` will match just `"ab"`.

#### **Caveat: Catastrophic Backtracking**

A poorly written regex with nested quantifiers and alternation can lead to "catastrophic backtracking," where the regex engine's execution time grows exponentially with the input string length. This can cause severe performance degradation and has been the source of real-world outages (e.g., a notable Cloudflare incident) and denial-of-service vulnerabilities. Always be cautious with complex regexes, especially on untrusted user input. Python's `re` module does not have a built-in timeout mechanism.