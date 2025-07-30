This document contains the lecture notes for the Shell scripting module, covering shell fundamentals, programming constructs, advanced features, and an introduction to the first assignment.

### **Lecture 1: Introduction to Shell Scripting**

This lecture provides a foundational understanding of what a shell is, the specific shell (`dash`) used in this course, and the critical sequence of operations a shell performs when processing a command line. Understanding this sequence is paramount, as it is a common source of bugs and security vulnerabilities.

#### **1.1. The Shell: An Overview**

A shell serves two primary functions:

1.  **Interactive Command Line Interpreter**: This is the most familiar use case, where a user types commands at a prompt, and the shell executes them. These commands typically involve running other programs (e.g., `dcc`, `ls`, `cp`) or manipulating the file system.
2.  **Programming Language**: The shell can be used to write scripts—programs that automate sequences of commands. This is a powerful tool for system administration, build automation, and creating custom utilities.

While graphical user interfaces (GUIs) offer an easier entry point for new users, command-line interfaces (CLIs), though requiring more initial learning, are significantly more powerful and are the focus of this course.

**Slide Cross-reference**: Slides 2, 3.

#### **1.2. Choice of Shell: `dash` and POSIX Compliance**

Numerous shells are available on Unix-like systems, with `bash` being the most popular for interactive use. Other common shells include `zsh`, `fish`, and `ash`. To ensure that the skills learned are broadly applicable and that scripts are portable, this course adheres to the **POSIX standard** for shell features.

The `dash` shell is used for all scripts in this course because it closely implements the POSIX standard. Code written for `dash` is generally compatible with other shells like `bash` and `zsh`, which implement a superset of the POSIX features. This focus on a core, standardized set of features ensures that the scripts you write will function correctly in diverse environments, from embedded systems (which often use `ash` via BusyBox) to automated CI/CD pipelines and system boot scripts.

**Caveats**: While the goal is universal compatibility, minor differences between shells can still exist. The course simplifies this by mandating `dash` compatibility. There will not be exam questions about whether a specific feature is POSIX-compliant.

**Slide Cross-reference**: Slide 2.

#### **1.3. The Shell's Order of Operations**

When a shell processes a line of input, it applies a series of transformations in a specific, crucial order. A misunderstanding of this sequence is a frequent cause of bugs and significant security vulnerabilities. The lecturer notes that major security exploits, costing billions in total, have arisen from shell programmers not understanding this process.

The sequence of transformations is as follows:

1.  **Tilde Expansion**: The tilde character (`~`) is expanded.
    *   `~` expands to the current user's home directory.
    *   `~username` expands to the home directory of `username`.
    *   **Example**: `echo ~` might expand to `echo /home/z1234567`. `echo ~root` expands to `/root`. This transformation is generally straightforward and does not cause security issues.
2.  **Parameter and Variable Expansion**: Variables, denoted by a leading dollar sign (`$`), are replaced with their values.
    *   **Syntax**: `name=value` (note: no spaces around the equals sign). `echo $name`.
    *   **Untyped Variables**: Shell variables are effectively untyped strings. `x=1` and `x="1"` are treated similarly. This lack of a strong typing system means the shell does not provide the same level of error-checking as languages like C or Python, making it less suitable for large, complex programs.
    *   **Uninitialized Variables**: If a variable is not set, it expands to an empty string with no error message. This can lead to silent bugs from typos in variable names.
    *   **Example**:
        ```bash
        Dylan=great
        Anna=wonderful
        echo $Dylan $Anna
        # Output: great wonderful
        
        # Misspelled variable
        echo $Dilan
        # Output: (nothing, just a newline)
        ```
    *   **Global Scope**: By default, shell variables have a single global scope. A variable defined anywhere can be accessed or modified anywhere else in the script (outside of subshells), which is a significant drawback for large programs.
3.  **Arithmetic Expansion**: Arithmetic expressions are evaluated.
    *   **Syntax**: `$((expression))`. The shell evaluates the integer arithmetic expression within the double parentheses.
    *   **Performance**: Shell arithmetic is significantly slower than in compiled languages like C. The shell must convert string variables to numbers, perform the operation, and convert the result back to a string. This involves thousands of machine instructions, whereas a C integer addition might be a single instruction. Therefore, the shell is not suitable for computationally intensive tasks.
    *   **Example**:
        ```bash
        Dylan=6
        Anna=12
        echo $(($Dylan + $Anna))
        # Output: 18
        
        # Variables can be used without the '$' inside
        echo $(($Dylan + Anna))
        # Output: 18
        ```
4.  **Command Substitution**: The output of a command replaces the command itself.
    *   **Syntax**: `$(command)`. The shell executes `command`, captures its standard output (stripping trailing newlines), and substitutes the `$(command)` construct with that output.
    *   **Legacy Syntax**: An older syntax using backticks (`` `command` ``) is equivalent but is not recommended as it does not nest well. You will encounter it in older scripts.
    *   **Quoting**: It is almost always correct to enclose command substitutions in double quotes (`"$(command)"`). This prevents the shell's subsequent word-splitting step from breaking up output that contains spaces or newlines.
    *   **Example**:
        ```bash
        # Assign the current date and time to a variable
        current_time="$(date)"
        echo "The time is: $current_time"
        
        # Use a pipeline inside the substitution
        time_zone="$(date | sed 's/.* \([A-Z]*\) .*/\1/')"
        echo "Timezone: $time_zone"
        ```
5.  **Word Splitting**: The shell breaks the processed line into "words" (arguments) based on whitespace characters. This is a primary reason why quoting is so important. Unquoted variables or command substitutions containing spaces will be split into multiple arguments.
6.  **Filename Expansion (Globbing)**: The shell interprets special characters (`*`, `?`, `[]`) as patterns to match against filenames in the current directory. This is distinct from regular expressions.
7.  **I/O Redirection**: The shell processes input/output redirection operators (e.g., `>`, `<`, `|`).
8.  **Command Execution**: The first word is identified as the command to run, and the subsequent words are passed as its arguments (`argv[1]`, `argv[2]`, etc.). The shell then searches the directories listed in the `PATH` environment variable to find the executable file for the command.

**Slide Cross-reference**: Slides 3, 4, 8, 9, 13, 14.

#### **1.4. Quoting in the Shell**

Quoting is used to control which transformations the shell applies. The shell has two primary types of quotes, which have different meanings from their counterparts in Python or C.

*   **Single Quotes (`''`)**: These are the strongest quotes. No transformations of any kind occur inside single quotes. Everything between them is treated as a literal string. The only character that cannot appear inside single quotes is a single quote itself.
    *   **Example**: `echo 'The value of $HOME is $HOME'` will literally print `The value of $HOME is $HOME`.

*   **Double Quotes (`""`)**: These are weaker quotes. They prevent word splitting and globbing but still allow variable expansion, arithmetic expansion, and command substitution. This makes them ideal for protecting variables that might contain spaces.
    *   **Example**:
        ```bash
        file_list="$(ls)"
        echo "$file_list" 
        # Preserves newlines from ls output
        
        echo "The value of \$HOME is $HOME"
        # The backslash escapes the first '$', but the second is expanded.
        # Output: The value of $HOME is /home/z1234567
        ```

**Slide Cross-reference**: Slides 10, 11.

#### **1.5. Here Documents (`<<`)**

A "here document" is a mechanism for providing a multi-line string as standard input to a command.

*   **Syntax**: `command <<END_MARKER` followed by lines of text, terminated by a line containing only `END_MARKER`.
*   **Expansion**: By default, variables and commands are expanded within the here document, similar to double quotes.
*   **Disabling Expansion**: If the `END_MARKER` is quoted (e.g., `<<'END_MARKER'`), no expansion occurs, similar to single quotes.

**Example**:
```bash
name=Andrew
tr 'a-z' 'A-Z' <<END_MARKER
Hello $name
How are you
END_MARKER
# Output:
# HELLO ANDREW
# HOW ARE YOU
```
This is a feature you may encounter in existing scripts, though it is less commonly needed for beginner tasks.

**Slide Cross-reference**: Slide 12.

#### **1.6. Shell Globbing versus Regular Expressions**

Globbing is the shell's mechanism for filename matching. It uses a syntax that is confusingly similar to, but simpler and less powerful than, regular expressions (regex).

| Feature         | Globbing Pattern | Regex Equivalent | Description                        |
| --------------- | ---------------- | ---------------- | ---------------------------------- |
| Any characters  | `*`              | `.*`             | Matches zero or more characters.   |
| Single character| `?`              | `.`              | Matches exactly one character.     |
| Character class | `[abc]`          | `[abc]`          | Matches `a`, `b`, or `c`.          |
| Inverted class  | `[!abc]`         | `[^abc]`         | Matches any character except `a`, `b`, or `c`. |

A critical difference in behaviour:
*   **Non-matching Globs**: If a glob pattern does not match any files, the shell, by default, leaves the pattern string unchanged and passes it as a literal argument to the command.
*   **Security/Bug Implication**: This behaviour is extremely dangerous when passing regexes to commands like `grep` or `sed`. If a regex containing glob characters (like `*`) is left unquoted and happens to not match any filenames, it will be passed correctly to the command. However, if a user later creates a file whose name matches the glob pattern, the shell will expand the pattern into a list of filenames *before* passing it to `grep`, causing the command to fail or behave unexpectedly.
*   **The Golden Rule**: **Always enclose regular expressions in single quotes** when passing them as arguments on the command line to prevent the shell from interpreting them as globs.

**Example of a catastrophic bug**:
```bash
# This seems to work if no file named main.text exists
grep 'main.*' some_file.txt

# A user creates a file
touch main.text

# The next time the command is run, it becomes:
grep main.text some_file.txt 
# The regex is gone, and the command's meaning has completely changed.
```
**Correct Usage**:
```bash
grep 'main.*' some_file.txt
```

**Slide Cross-reference**: Slide 15.

### **Lecture 2: Shell Control Flow and Scripting Fundamentals**

This lecture builds upon the fundamentals by introducing control flow structures (`if`, `while`), the concept of exit status, script arguments, and file permissions. It provides practical examples of building simple but useful shell scripts.

#### **2.1. File Permissions and `chmod`**

On Unix-like systems, to execute a file as a script, it must have the "execute" permission set. File permissions are managed by the `chmod` (change mode) command.

*   **Permissions**: There are three primary types of permissions:
    *   `r` (read): Permission to view the contents of a file.
    *   `w` (write): Permission to modify the contents of a file.
    *   `x` (execute): Permission to run the file as a program or script.
*   **Groups**: These permissions are set for three distinct groups: the user (owner), the group, and others.
*   **`chmod` Usage**: The command can be used with symbolic notation to modify permissions.
    *   **Example**: To add execute permission for the user (owner) to a script named `hello.sh`:
        ```bash
        chmod u+x hello.sh
        ```

**Slide Cross-reference**: Slide 20 (Implicitly, via `chmod 755`).

#### **2.2. Exit Status: The Heart of Shell Control Flow**

When a Unix program terminates, it returns a small integer value to its parent process, known as its **exit status**. This mechanism is the foundation of control flow in shell scripting.

*   **Convention**:
    *   **`0`**: Indicates success. The program completed its task without error.
    *   **Non-zero (typically `1`)**: Indicates failure. An error occurred.
*   **Special Variable `$?`**: The shell stores the exit status of the most recently executed command in the special variable `$?`.
*   **`if`/`while` Control**: The `if` and `while` constructs in the shell do not evaluate a boolean expression directly. Instead, they execute a command and make a decision based on its exit status. If the exit status is `0` (success), the condition is considered true. If it is non-zero (failure), the condition is considered false.

**Helper Commands for Control Flow**:
*   `true`: A command that does nothing and always exits with status `0`.
*   `false`: A command that does nothing and always exits with status `1`.
*   `test` (or `[`): A command designed specifically to evaluate expressions and return an exit status. It performs string comparisons, numeric comparisons, and file attribute checks.

**Example**:
```bash
gcc my_program.c
echo "Exit status of gcc was: $?"

if gcc my_program.c
then
    echo "Compilation successful."
else
    echo "Compilation failed."
fi
```

**Slide Cross-reference**: Slides 26, 27, 28, 29, 31.

#### **2.3. I/O Redirection and `/dev/null`**

Unix programs typically have two output streams: standard output (`stdout`) for normal output and standard error (`stderr`) for error messages and diagnostics.

*   **Redirection Operators**:
    *   `>`: Redirect `stdout` to a file (overwrites existing file).
    *   `>>`: Append `stdout` to a file.
    *   `2>`: Redirect `stderr` to a file.
    *   `2>>`: Append `stderr` to a file.
    *   `2>&1`: Redirect `stderr` to the same destination as `stdout`.
*   `/dev/null`: A special file that acts as a "black hole". Any data written to it is discarded. This is useful for silencing unwanted output from a command.

**Example**: To run `gcc` but discard all its diagnostic messages, leaving only the exit status for an `if` statement:
```bash
if gcc my_program.c >/dev/null 2>&1
then
    echo "It compiles!"
else
    echo "It does not compile."
fi
```

**Slide Cross-reference**: Slide 16.

#### **2.4. Control Structures: `if` and `while`**

*   **`if` statement**:
    ```bash
    if command
    then
        # commands to run if 'command' succeeds (exit status 0)
    elif another_command
    then
        # commands to run if 'another_command' succeeds
    else
        # commands to run if all previous commands fail
    fi 
    ```

*   **`while` loop**:
    ```bash
    while command
    do
        # commands to run as long as 'command' succeeds
    done
    ```
    *   **Anti-social loops**: A loop like `while true` will run as fast as possible, consuming 100% of a CPU core. To prevent this, the `sleep` command should be used to introduce a pause. `sleep 5` will pause execution for 5 seconds.

**Example**: A script that repeatedly checks if a C file compiles.
```bash
#!/bin/dash
while true
do
    if gcc hello_anna.c >/dev/null 2>&1
    then
        echo "hello_anna.c is correct C"
    else
        echo "Error in hello_anna.c"
    fi
    sleep 5 # Check every 5 seconds
done
```

**Slide Cross-reference**: Slides 29, 30, 31.

#### **2.5. Shell Script Arguments**

Shell scripts can access their command-line arguments using special variables:

*   `$0`: The name of the script itself.
*   `$1`, `$2`, ...: The first, second, etc., arguments.
*   `$#`: The total number of arguments.
*   `"$@"`: All arguments, with each argument treated as a separate, quoted word. This is the correct and safe way to pass all of a script's arguments on to another command.

**Good Practice**: For readability and maintainability, it is highly recommended to assign positional parameters like `$1` and `$2` to named variables at the beginning of your script.

**Example**: The `seq.sh` script, which prints a sequence of numbers.
```bash
#!/bin/dash
# Print integers from <first> to <last>

# Argument checking
if [ "$#" -eq 1 ]; then
    first=1
    last="$1"
elif [ "$#" -eq 2 ]; then
    first="$1"
    last="$2"
else
    # Error messages should go to stderr.
    echo "Usage: $0 [<first>] <last>" 1>&2
    exit 1
fi

# Main loop
i="$first"
while [ "$i" -le "$last" ]; do
    echo "$i"
    i=$((i + 1))
done

exit 0 # Indicate success
```

**Slide Cross-reference**: Slides 21, 22, 32, 33, 34.

#### **2.6. Case Study: `watch_website.sh`**

This example demonstrates a practical script that monitors a web page for a specific string and sends a notification.

*   **Core Tool**: `curl` is a command-line tool for transferring data with URLs. `curl --silent <url>` fetches the content of the URL and prints it to standard output without showing progress meters.
*   **Logic**:
    1.  Use a `while true` loop for continuous monitoring.
    2.  Inside the loop, use `curl` to fetch the web page content.
    3.  Pipe the content to `grep` to search for the desired pattern.
    4.  Use an `if` statement that checks the exit status of `grep`. `grep` exits with `0` if it finds a match.
    5.  If a match is found, send a notification (e.g., using `mail`) and exit the script.
    6.  If no match is found, `sleep` for a set interval before the next check to avoid overwhelming the web server.

This case study brings together loops, conditional logic, command-line tools (`curl`, `grep`), and best practices like rate-limiting.

**Slide Cross-reference**: Slides 35, 36.

### **Lecture 3: Advanced Shell Scripting Constructs**

This lecture explores more advanced shell features, including the `for` loop, different ways to combine commands, command grouping, static analysis with `shellcheck`, and the `case` statement.

#### **3.1. The `for` Loop**

The `for` loop iterates over a list of words. Its structure is very similar to a Python `for` loop.

*   **Syntax**:
    ```bash
    for var in word1 word2 word3 ...
    do
        # Commands using $var
    done
    ```
*   **Common Usage**: It is often used to iterate over the command-line arguments (`for filename in "$@"`) or the output of a command substitution (`for i in $(seq 1 10)`).

**Slide Cross-reference**: Slide 37, 38.

#### **3.2. Conditional Execution with `&&` and `||`**

The `&&` (AND) and `||` (OR) operators provide a concise alternative to `if` statements for chaining commands based on their exit status.

*   `command1 && command2`: `command2` is executed **only if** `command1` succeeds (exits with status 0).
*   `command1 || command2`: `command2` is executed **only if** `command1` fails (exits with a non-zero status).

**Key Use Case**: These are essential for writing robust scripts that perform destructive actions. A common pattern is to ensure a directory change succeeds before removing files.
```bash
# Unsafe: If cd fails, rm will run in the original directory!
cd /path/to/tempdir
rm -rf *

# Safe: rm only runs if cd was successful.
cd /path/to/tempdir && rm -rf *
```

**Slide Cross-reference**: Slides 39, 40.

#### **3.3. Command Grouping: `{}` vs. `()`**

To apply conditional logic or redirection to a sequence of commands, they must be grouped.

*   **Curly Braces (`{ ... }`)**: Executes the commands in the **current shell environment**. Any changes to variables or the current directory will persist after the group finishes. A semicolon or newline is required before the closing brace.
*   **Parentheses (`( ... )`)**: Executes the commands in a **subshell**. This creates a new, separate shell process. Any changes to variables or the current directory are discarded when the subshell exits.

**Example**:
```bash
x=123
(cd /tmp; x=abc)
echo $x # Prints 123, the change was lost
pwd      # Still in the original directory

x=123
{ cd /tmp; x=abc; }
echo $x # Prints abc, the change persisted
pwd      # Now in /tmp
```
For most use cases where you want to group commands within a script, curly braces are the correct choice. Subshells are useful when you want to perform a set of actions in a different context (like a different directory) without affecting the main script.

**Caveat**: Commands in a pipeline (e.g., `cmd1 | cmd2`) are also executed in subshells.

**Slide Cross-reference**: Slide 41.

#### **3.4. Static Analysis with `shellcheck`**

`shellcheck` is a static analysis tool that examines shell scripts for common errors and bad practices without running the code. It is an invaluable tool for catching bugs early.

*   **Common Errors Detected**:
    *   Unquoted variables that could cause word splitting issues.
    *   Using a variable that was never assigned a value (potential typo).
    *   Dangerous command sequences (like the `cd`/`rm` example above).
    *   Incorrect use of `test`/`[`.

It is highly recommended to run `shellcheck` on all your scripts. It is available on CSE systems and will be used by some of the automated testing for your assignments.

**Slide Cross-reference**: Slide 42.

#### **3.5. Reading Input with `read`**

The `read` built-in command reads a single line from standard input and assigns it to one or more variables.

*   **Syntax**: `read var1 var2 ...`
*   **Behavior**: It reads a line, splits it into words based on whitespace, and assigns the words to the specified variables. The last variable receives all remaining words on the line.
*   **Pitfalls**:
    *   By default, `read` can mangle input containing backslashes. Use `read -r` to prevent this.
    *   By default, `read` strips leading and trailing whitespace. To preserve it, unset the `IFS` (Internal Field Separator) variable for the duration of the command: `IFS= read -r line`.

**Example**: A simple interactive script.
```bash
echo -n "Do you like learning Shell? "
read answer
# Process the answer...
```

**Slide Cross-reference**: Slides 45, 46, 47.

#### **3.6. The `case` Statement**

The `case` statement provides a way to match a word against several patterns, offering a readable alternative to a long chain of `if`/`elif` statements.

*   **Syntax**:
    ```bash
    case "$word" in
        pattern1)
            commands1
            ;;
        pattern2|pattern3) # Can match multiple patterns
            commands2
            ;;
        *) # Default case, matches anything
            default_commands
            ;;
    esac
    ```
*   **Patterns**: The patterns use the same globbing syntax (`*`, `?`, `[]`) as filename expansion, not regular expressions.
*   **Relevance**: While `case` statements are not essential (any `case` can be rewritten with `if`), they can improve code clarity and are found in many existing scripts. You should be able to read and understand them.

**Slide Cross-reference**: Slides 48, 49, 50, 51.

### **Lecture 4: Advanced Scripting Techniques and Assignment 1 Introduction**

This lecture covers shell functions in more detail, presents a sophisticated plagiarism detection case study, and introduces Assignment 1. It also delves into robust temporary file handling and parallel processing.

#### **4.1. Shell Functions**

Functions allow you to group code for reuse, improving structure and readability.

*   **Syntax**:
    ```bash
    function_name() {
        # commands
    }
    ```
*   **Arguments**: Accessed inside the function using `$1`, `$2`, `"$@"`, etc., just like script arguments. These shadow the script's main arguments.
*   **Return Value**: Functions return an exit status. The `return` command is used to exit a function and specify its status (e.g., `return 0` for success). **Crucially, `exit` will terminate the entire script, not just the function.**
*   **Variable Scope**: By default, variables are global. To create a function-specific variable, you **must** declare it with the `local` keyword. Forgetting `local` is a common and difficult-to-debug error, as a function can unintentionally modify a variable used elsewhere in the script.

**Example**: A function to check for primality, demonstrating the need for `local`.
```bash
#!/bin/dash

is_prime() {
    local n i # CRITICAL: i and n are local to this function
    n=$1
    
    i=2
    while [ "$i" -lt "$n" ]; do
        if [ $((n % i)) -eq 0 ]; then
            return 1 # Not prime, return failure
        fi
        i=$((i + 1))
    done
    return 0 # Prime, return success
}

# This loop would break if 'i' in is_prime was not local
i=2
while [ "$i" -lt 100 ]; do
    if is_prime "$i"; then
        echo "$i"
    fi
    i=$((i + 1))
done
```

**Slide Cross-reference**: Slides 55, 56, 57.

#### **4.2. Case Study: A Plagiarism Detector**

This extended example illustrates how to build a progressively more robust script to detect copied code. It showcases several important techniques for data normalization.

1.  **Initial Approach (Pairwise `diff`)**: A nested loop compares every file with every other file using `diff`. This is inefficient (O(n²)) and easily fooled.
2.  **Ignoring Trivial Changes**: The `diff` command's options are used to ignore differences in whitespace (`-w`), blank lines (`-B`), and case (`-i`).
3.  **Ignoring Comment/Variable Name Changes (Normalization)**: Since `diff` cannot ignore semantic changes like altered comments or variable names, the files are first transformed into a **canonical form** using `sed`.
    *   A `sed` command (`sed 's/\/\/.*//'`) removes all C-style comments.
    *   Another `sed` command replaces all identifiers with a generic placeholder (e.g., "v"), effectively ignoring variable name changes.
4.  **Ignoring Function Reordering**: To handle cases where functions are simply reordered, the transformed file content is piped through `sort` before the final `diff`. This ensures that two files with the same lines, regardless of order, will appear identical.
5.  **A More Efficient Approach (Hashing)**: The O(n²) pairwise comparison is inefficient for large numbers of files. A much faster (O(n)) approach involves hashing:
    *   For each file, generate its canonical form (remove comments, normalize variables, sort lines).
    *   Calculate a **cryptographic hash** (e.g., using `sha256sum`) of the canonical form. A cryptographic hash is a fixed-size "fingerprint" of the data.
    *   Files with identical canonical forms will produce the exact same hash.
    *   By hashing all files, sorting the list of hashes, and using `uniq -d` to find duplicates, we can identify copied files in a single pass.

**Slide Cross-reference**: Slides 58, 59, 61, 62, 63, 65, 66.

#### **4.3. Robust Temporary Files: `mktemp` and `trap`**

Scripts often need temporary files. Creating them with hardcoded names (e.g., `/tmp/temp1`) is insecure and fragile.

*   **`mktemp`**: This command securely creates a new, empty temporary file with a unique, unguessable name and prints the name to standard output. This is the correct way to create temporary files.
*   **`trap`**: This command allows a script to "trap" signals or events and execute a specific command. It is essential for cleanup. The pattern `trap 'rm -f "$TEMP_FILE1" "$TEMP_FILE2"' EXIT` ensures that the specified temporary files will be removed when the script exits for any reason (normally, via an error, or via an interrupt like Ctrl-C).

**Correct Pattern for Temporary Files**:
```bash
#!/bin/dash

# Put trap first so it works even if mktemp fails.
trap 'rm -f "$TMP_FILE1" "$TMP_FILE2"' EXIT

TMP_FILE1=$(mktemp)
TMP_FILE2=$(mktemp)

# ... use the temporary files ...
```

**Slide Cross-reference**: Slides 60, 64, 68.

#### **4.4. Asynchronous Execution and Parallelism**

Shell scripts can run commands in parallel to speed up tasks on multi-core CPUs.

*   **Backgrounding (`&`)**: Appending an ampersand (`&`) to a command runs it in the background. The script does not wait for it to finish and continues immediately.
*   **`wait`**: The `wait` command pauses the script until all backgrounded child processes have completed. This is crucial for synchronizing steps, e.g., waiting for all files to compile before linking them.
*   **`xargs -P`**: `xargs` provides a robust and convenient way to manage parallelism. The `-P <num>` option tells `xargs` to run up to `<num>` processes in parallel. This is superior to a simple `&` loop because it limits resource usage.
    *   To find the number of available cores, you can use `getconf _NPROCESSORS_ONLN`.
*   **GNU `parallel`**: A more powerful and feature-rich alternative to `xargs` for managing parallel execution.

**Example**: Compiling 1001 C files in parallel.
```bash
# Get number of CPU cores, default to 8 if not found.
max_processes=$(getconf _NPROCESSORS_ONLN 2>/dev/null) || max_processes=8

# Compile all .c files into .o files, running up to $max_processes in parallel.
echo *.c | xargs -P"$max_processes" -n1 clang -c

# Link all the resulting .o files into the final binary.
clang -o binary -- *.o
```

**Slide Cross-reference**: Slides 67, 69, 70, 71, 72, 73, 74.

#### **4.5. Introduction to Assignment 1**

Assignment 1 requires you to build a simplified assignment submission and marking system, similar to `give` and `autotest`. This is a practical, real-world application of shell scripting.

*   **Core Task**: You will write eight shell scripts (`my_give-add`, `my_give-submit`, etc.) that work together to manage assignments.
*   **State Management**: The scripts must store persistent information (e.g., which assignments exist, who has submitted what) in a hidden directory named `.my_give`.
*   **Reference Implementation**: A working version of the solution is provided. If the specification is unclear, you can run the reference implementation to see the expected behavior. Your submission must match its output and behavior.
*   **Test Files (`.test`)**: Test specifications are provided in `.test` files, which are **tar archives**. Your scripts will need to use the `tar` command to extract and interpret the contents of these files to run tests.
*   **Constraints**:
    *   All scripts must be POSIX-compliant (i.e., work with `/bin/dash`).
    *   You may only use a specified whitelist of external programs.
*   **Recommendation**: Start early. Read the specification carefully. Use the reference implementation to clarify requirements. Build your test suite as you develop. Use `shellcheck` frequently.