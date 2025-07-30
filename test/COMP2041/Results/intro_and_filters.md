These notes provide a comprehensive summary of the introductory lectures for COMP2041/9044, covering course administration, the philosophy of Unix filters, and the practical application of regular expressions and shell scripting.

### **Part I: Course Introduction (COMP2041/9044)**

#### **1.0. Overview and Rationale**

The course, COMP2041/COMP9044 Software Construction, is designed to bridge the gap between introductory programming courses and the practical demands of building software. First-year courses typically focus on a single language (C or Python), small, tightly-specified problems, and narrow programming aspects. This course expands upon that foundation by introducing multiple languages, the combination of multiple programs to solve larger and less-specified problems, and the use of essential software development tools and system configuration.

The primary outcome is to equip students with the practical skills necessary to build a software package, host it on a platform like GitHub, and enable others to download and use it. The emphasis is on expanding software-building capabilities beyond simple coding.

*   **Slide Cross-reference:** Course Goals (Slide 3/20), Course Goals - TLDR (Slide 4/20).

#### **1.1. Course Staff**

The course is supported by a large teaching team, which includes:
*   **Convenor & Lecturer:** Andrew Taylor
*   **Administration:** Dylan Brotherston and Anna Brew, who manage back-end logistics and tutor recruitment.
*   **Tutors:** A large team of past students who have successfully completed the course. They lead tutorials and labs and answer questions on the course forum.

*   **Slide Cross-reference:** COMP(2041|9044) Staff (Slide 2/20).

#### **1.2. Assumed Knowledge and Prerequisites**

Students are expected to have completed a first programming course and be able to write, debug, and test programs in either C (e.g., from COMP1511) or Python (e.g., from COMP9021).

*   **C Knowledge:** Very little C knowledge is assumed. While some examples may be in C, it is not a primary focus, and students without a C background will not be disadvantaged.
*   **Python Knowledge:** Basic Python knowledge is assumed, equivalent to what might be gained from courses like COMP9021 or older versions of COMP1531 (pre-2022). Students with zero Python experience are strongly advised to undertake self-study during the first few weeks of the term, utilising the abundant online resources available. The course forum is a suitable place to ask for recommendations on introductory Python courses.

*   **Slide Cross-reference:** Assumed Knowledge (Slide 5/20).

#### **1.3. Course History and Evolution**

To provide context for students who may have seen older course descriptions, the following changes have occurred in recent years:

*   **Web Programming:** The front-end and back-end web programming components have been moved to a separate course, COMP6080. This course will only touch upon the web by scripting the scraping of web data.
*   **Perl:** The course was formerly taught using Perl. It has since transitioned to Python, as Python has become more ubiquitous for the types of scripting and system tasks covered. No Perl is taught or required in the current iteration.
*   **Python Prerequisite:** The course previously relied on COMP1531 to teach Python. As COMP1531 now uses JavaScript, students without a Python background must learn the basics independently.

*   **Slide Cross-reference:** Changes from recent years (Slide 6/20).

#### **1.4. Course Logistics**

**1.4.1. Lectures**
*   **Schedule:** Lectures are held on Mondays (in-person) and Thursdays (online via YouTube). Public holidays may alter this schedule, with replacement lectures announced via email.
*   **Format:** The lecturer, Andrew Taylor, emphasises practical, live-coding demonstrations to solve problems, supplemented with theory, historical context, and motivation.
*   **Interaction:** Students watching the live-streamed lectures are encouraged to ask questions in the chat, as this enhances the experience for both live viewers and those watching the recordings.
*   **Recordings:** All lectures are recorded. In-person lectures are available on Echo360 shortly after delivery and uploaded to YouTube the following day. Online lectures are available on YouTube immediately after the live stream.
*   **Slides:** Lecture slides are available on the course website before each lecture, though they may be subject to minor updates a few hours prior.

*   **Slide Cross-reference:** Lectures (Slide 7/20).

**1.4.2. Tutorials and Labs**
*   **Structure:** A three-hour weekly slot comprises a one-hour tutorial followed by a two-hour lab. This format is identical to COMP1511.
*   **Tutorials:** Tutorials are interactive sessions designed to clarify lecture concepts and prepare students for the weekly lab exercises or assignments. They are not mini-lectures. To maximise their benefit, students should review the tutorial questions beforehand. Active participation, including asking questions and contributing to discussions, is crucial. Tutors may not cover every question, and solutions are released on the Friday after the last tutorial.
*   **Labs:** Lab exercises are individual work and constitute 15% of the final mark. It is recommended to start the exercises before the lab session to make effective use of the tutors' assistance for more challenging problems. Labs include optional, and sometimes intentionally abstruse, challenge exercises. Full marks are generally achievable without completing all challenge exercises (the exact formula is in the course outline).

*   **Slide Cross-reference:** Tutorials (Slide 8/20), Lab Classes (Slide 9/20).

**1.4.3. Help Sessions**
Help sessions are available for assistance with assignments. The schedule is linked on the course homepage. These sessions become very busy in the days leading up to an assignment deadline, so starting assignments early is highly recommended to ensure help is accessible.

**1.4.4. Course Forum**
The course forum is the primary channel for questions. Most queries receive faster responses there from tutors or fellow students. Personal or private matters should be directed to the course email address.

#### **1.5. Assessment**

**1.5.1. Overview and Breakdown**
The assessment structure is as follows:
*   **Lab Exercises:** 15%
*   **Weekly Tests:** 10%
*   **Assignment 1:** 15% (Due Monday of Week 7, after Flex Week)
*   **Assignment 2:** 15% (Due Monday of Week 11)
*   **Final Exam:** 45%

*   **Slide Cross-reference:** Assessment (Slide 19/20).

**1.5.2. Lab Exercises**
Lab work is submitted via the `give` command before noon on the Monday of the following week. An extended deadline is provided for the first week's lab to accommodate late enrolments.

**1.5.3. Weekly Tests**
Starting from Week 3, weekly programming tests are conducted under self-enforced exam conditions with a one-hour time limit. The best 6 of 8 tests contribute to the final grade.

*   **Slide Cross-reference:** Weekly Tests (Slide 10/20).

**1.5.4. Assignments**
There are two individual assignments. Students are strongly urged to start early to avoid the last-minute rush for help sessions.

*   **Slide Cross-reference:** Assignments (Slide 11/20).

**1.5.5. Final Exam and Hurdle Requirement**
The final exam is a practical, in-person lab exam held during the official examination period. It assesses the core coding skills of the course, primarily in shell and Python.

*   **Hurdle Requirement:** Students **must score at least 18 out of 45 (40%)** on the final exam to be eligible to pass the course, regardless of their overall mark. This ensures that a passing grade reflects a genuine mastery of the course's practical skills.

*   **Slide Cross-reference:** Final Exam (Slide 18/20), Assessment (Slide 19/20).

**1.5.6. Late Penalties and Solution Release**
*   **Late Penalty:** The standard UNSW late penalty is applied to all assessments. A deduction of 0.2% of the maximum mark for the assessment is made for each hour (or part thereof) that the submission is late. Submissions are not accepted more than five days late.
*   **Solution Release:** Due to the late submission policy and potential special consideration extensions, sample solutions and marks for labs and tests are typically released around two weeks after the original deadline.

*   **Slide Cross-reference:** Late Penalties (Slide 12/20), Sample Solutions and Marking (Slide 13/20).

#### **1.6. Policies and Conduct**

**1.6.1. Code of Conduct**
Students are expected to maintain a respectful, polite, and civil demeanour towards teaching staff and fellow students. Any form of racist, sexist, offensive, or bullying behaviour will not be tolerated. Students who witness such behaviour are encouraged to report it to a member of the teaching staff.

Additionally, a strict professional boundary must be maintained with tutors. Tutors are instructed by CSE policy not to socialise with individual students. Students must not ask tutors for social engagements.

*   **Slide Cross-reference:** Code of Conduct (Slide 14/20).

**1.6.2. Academic Integrity and Plagiarism**
This course has **zero group work**. All submitted work must be entirely the student's own.
*   **Prohibited Actions:** Reading another student's code, showing your code to another student before submission, and paying for solutions are all considered serious academic misconduct.
*   **Ethical Standpoint:** Submitting work under one's own name is a claim of authorship. Including code written by others without attribution is dishonest.
*   **Consequences:** The university treats plagiarism very seriously. Penalties can include suspension from UNSW and the loss of scholarships. Electronic plagiarism detection tools are used.

*   **Slide Cross-reference:** Plagiarism (Slides 15/20, 16/20).

**1.6.3. Use of Generative AI**
*   **Dilemma for Learners:** While tools like GitHub Copilot and ChatGPT are used by professional software engineers, they pose a risk for learners. These tools can generate code with subtle errors or security vulnerabilities that only an expert can identify and correct. Over-reliance on these tools can impede the development of the fundamental understanding required to use them safely and effectively.
*   **Course Policy:** The use of generative AI tools is **not permitted** in this course, with a potential exception for assignments where small, attributed use may be allowed (this will be specified in the assignment specification). The primary reason is that these tools are not available in the final exam, and students must be able to code proficiently without them. Other courses may have different policies.

*   **Slide Cross-reference:** Use of Generative AI Tools (Slide 17/20).

#### **1.7. Advice for Success**
Success in this course is directly correlated with practice. It is a practical, hands-on course that requires a significant time commitment to coding. Students who enjoy coding and problem-solving will likely find the course rewarding.
*   **Practice:** Go beyond the required lab exercises. Attempt extra tutorial questions. Code regularly.
*   **Time Management:** The workload intensifies in the second half of the term (Weeks 5-10). Start assignments early.
*   **Self-Reflection:** If you do not enjoy coding and do not see the future utility of these skills, it is worth reconsidering your enrolment in the course.

*   **Slide Cross-reference:** How to Pass this Course (Slide 20/20).

---

### **Part II: The Unix Philosophy: Filters and Pipelines**

#### **2.0. The Byte Stream and Text Encoding**

**2.0.1. Standard Streams (stdin, stdout, stderr)**
When a program runs on a Unix-like system, it is automatically connected to three fundamental data streams:
1.  **Standard Input (`stdin`):** The primary source of input data for the program, typically from the keyboard by default.
2.  **Standard Output (`stdout`):** The primary destination for the program's output, typically the terminal screen by default.
3.  **Standard Error (`stderr`):** A separate stream for diagnostic or error messages, also directed to the terminal screen by default. This separation allows error messages to be seen even if `stdout` is redirected to a file.

**2.0.2. Bytes vs. Characters (ASCII and UTF-8)**
A byte stream is fundamentally a sequence of bytes. A byte is a unit of digital information that most commonly consists of 8 bits, representing a value from 0 to 255. The interpretation of these bytes is what gives them meaning.

*   **ASCII (American Standard Code for Information Interchange):** An early character encoding standard that uses 7 bits to represent 128 characters, including the English alphabet (uppercase and lowercase), digits, and punctuation. It is sufficient for English but inadequate for most other world languages.
*   **UTF-8 (Unicode Transformation Format - 8-bit):** The dominant character encoding for the modern web. It is a variable-width encoding capable of representing every character in the Unicode standard, which encompasses all of the world's writing systems. While this course will primarily work with ASCII-like text, an awareness of UTF-8 and its implications is crucial for modern software development.

#### **2.1. Unix Filters**

**2.1.1. Definition and Core Pattern**
A **Unix filter** is a program designed to transform a byte stream. It adheres to a specific pattern:
1.  It reads bytes from its standard input (or from files specified as arguments).
2.  It performs a transformation on these bytes.
3.  It writes the transformed bytes to its standard output.

Most filters are line-based, meaning they process data one line at a time. The fundamental design principle is to create small, single-purpose programs that can be combined to perform complex tasks.

*   **Slide Cross-reference:** What is a filter? (Slide 2/62), Filter summary by type (Slide 62/62).

**Example: Filter Structure**
A common structure for a filter program is to check for command-line arguments.
*   If arguments are present, they are treated as file names, and each file is processed in sequence.
*   If no arguments are present, the program reads from standard input.

```c
// Simplified C structure for a filter
int main(int argc, char *argv[]) {
    if (argc == 1) {
        // No file arguments, process standard input
        process_stream(stdin);
    } else {
        // Process each file given as an argument
        for (int i = 1; i < argc; i++) {
            FILE *in = fopen(argv[i], "r");
            // ... error handling ...
            process_stream(in);
            fclose(in);
        }
    }
    return 0;
}
```

*   **Slide Cross-reference:** cat: implemented in C - where does input come from? (Slide 11/62).

**2.1.2. Command-Line Arguments and Options**
Filters are controlled via command-line arguments.
*   **Options:** Special arguments that modify a program's behaviour. By convention, they begin with a dash (`-`).
    *   **Short form:** A single dash followed by a letter (e.g., `-i`).
    *   **Long form:** Two dashes followed by a word (e.g., `--ignore-case`).
    *   The `--help` option is commonly used to display a summary of a command's options.
*   **Caveat:** A potential issue arises if a filename begins with a dash, as it may be misinterpreted as an option. While it is advisable not to name files this way, workarounds exist.

*   **Slide Cross-reference:** Filters: Options (Slides 6/62, 7/62).

**2.1.3. Shell I/O Redirection (`<`, `>`)**
The shell provides syntax to redirect the standard streams of a program.
*   `command < input.txt`: Redirects `stdin` to read from `input.txt`.
*   `command > output.txt`: Redirects `stdout` to write to `output.txt`, overwriting it if it exists.

*   **Slide Cross-reference:** Using Filters (Slide 3/62).

**2.1.4. Pipelines (`|`)**
The **pipe** (`|`) is a shell operator that connects the `stdout` of one command to the `stdin` of another. This allows for the chaining of filters to create powerful data processing workflows. The success of Unix-like systems (including Linux, macOS, and Android) is heavily attributed to this simple yet powerful mechanism for combining programs.

```sh
# Example of a pipeline
command1 | command2 | command3
```

*   **Slide Cross-reference:** Using Filters (Slide 4/62).

#### **2.2. Core Utility: `cat` (Concatenate)**

**2.2.1. Key Concepts**
The `cat` command is the "identity filter." It reads its input and writes it to its output unchanged. Its name is an abbreviation of "concatenate," as it can be used to concatenate multiple files to `stdout`. While not very useful as a filter on its own, it serves as a canonical example of filter structure and is often used in scripts to provide data to a pipeline.

**2.2.2. Options**
*   `-n`: Number all output lines.
*   `-A`: Display non-printing characters (useful for debugging whitespace issues).
*   `-s`: Squeeze multiple adjacent blank lines into a single blank line.

*   **Slide Cross-reference:** cat: some options (Slide 9/62).

**2.2.3. Examples (C and Python Implementations)**

The course provides sample implementations of `cat` in both C and Python to illustrate the core filter pattern and highlight language differences.

*   **C Implementation (`cat.c`):** This version operates on a byte-by-byte basis, making it a true byte stream transformer.

    ```c
    // write bytes of stream to stdout
    void process_stream(FILE *stream) {
        int byte;
        while ((byte = fgetc(stream)) != EOF) {
            if (fputc(byte, stdout) == EOF) {
                perror("cat:");
                exit(1);
            }
        }
    }
    ```
    *   **Slide Cross-reference:** cat: implemented in C - passing bytes from input to stdout (Slide 10/62).

*   **Python Implementation (`cat.py`):** This version is line-based and assumes the input is valid UTF-8 text. It is more concise and readable but less general than the C version.

    ```python
    def process_stream(stream):
        """
        copy bytes of f to stdout
        """
        for line in stream:
            print(line, end="")
    ```
    *   **Slide Cross-reference:** cat: implemented in Python (Slide 12/62).

---

### **Part III: Pattern Matching with Regular Expressions and `grep`**

#### **3.0. Introduction to Regular Expressions**

**3.0.1. Motivation and History**
While selecting lines containing a single, fixed string is useful, many tasks require matching against a *set* of strings, which can be large or even infinite. **Regular expressions (regex)** provide a concise and powerful notation for describing such sets.

*   **History:** The concept was developed by mathematician Stephen Kleene in the 1950s. It was later adapted for practical computing by Ken Thompson (a Turing Award winner) in the 1960s for use in text editors and compilers on the Unix system.

*   **Slide Cross-reference:** Matching Any of A Set of String (Slide 17/62).

**3.0.2. Core Concepts: Describing Sets of Strings**
It is most effective to think of a regular expression as a formal definition of a set of strings. Regular expressions are ubiquitous in modern computing, with libraries available in nearly every programming language and support in many command-line tools.

*   **Resources:** Websites like [regex101.com](https://regex101.com) and [regexr.com](https://regexr.com) are invaluable tools for both learners and experts to build, test, and understand regular expressions.

*   **Slide Cross-reference:** Regular Expressions (Slide 18/62), Regular Expression Examples (Slide 23/62).

#### **3.1. Regular Expression Syntax**

**3.1.1. Basic Syntax**
A minimal but complete set of regex operators includes:
*   **Literal Characters:** A character without special meaning matches itself (e.g., `a` matches the string "a").
*   **Repetition (`*`):** An asterisk matches zero or more repetitions of the preceding pattern (e.g., `b*` matches "", "b", "bb", etc.).
*   **Alternation (`|`):** A vertical bar matches either the pattern to its left or the pattern to its right (e.g., `perl|python` matches "perl" or "python"). It represents the union of two sets of strings.
*   **Grouping (`()`):** Parentheses are used to group sub-patterns, allowing operators like `*` and `|` to apply to a whole sequence.
*   **Escape (`\`):** A backslash removes the special meaning of the character that follows it (e.g., `\*` matches a literal asterisk).

*   **Slide Cross-reference:** Regular Expressions Basics (Slide 19/62).

**3.1.2. Single Character Matching (Convenience Syntax)**
*   **Wildcard (`.`):** A dot matches any single character.
*   **Character Set (`[]`):** Square brackets match any single character from the list inside them. Ranges can be used (e.g., `[a-z]`, `[0-9]`).
*   **Negated Character Set (`[^]`):** An up-arrow `^` at the start of a character set negates it, matching any single character *not* in the list.

*   **Slide Cross-reference:** Convenient Regular Expressions for matching Single Characters (Slide 20/62).

**3.1.3. Anchors**
Anchors are special characters that do not match characters themselves but assert a position in the string.
*   **Start of String (`^`):** Matches the beginning of the string/line (e.g., `^cat` matches "cat" only if it's at the start).
    *   **Caveat:** Note the dual meaning of `^`. Inside `[]`, it negates the set; outside, it anchors to the start.
*   **End of String (`$`):** Matches the end of the string/line (e.g., `cat$` matches "cat" only if it's at the end).

*   **Slide Cross-reference:** Anchoring Matches (Slide 21/62).

**3.1.4. Repetition Quantifiers (Convenience Syntax)**
*   `+`: Matches one or more repetitions.
*   `?`: Matches zero or one repetition (makes the preceding element optional).
*   `{n}`: Matches exactly *n* repetitions.
*   `{n,m}`: Matches between *n* and *m* repetitions.
*   `{n,}`: Matches *n* or more repetitions.

*   **Slide Cross-reference:** Convenient Regular Expressions for Repetition (Slide 22/62).

#### **3.2. Utility: `grep` (Global Regular Expression Print)**

**3.2.1. Key Concepts**
The `grep` command is a filter that prints lines from its input that contain a substring matching a given regular expression. Its name is an acronym: **G**lobally search for a **R**egular **E**xpression and **P**rint.

**3.2.2. Options**
*   `-E`: Use extended regular expression syntax (e.g., `|`, `+`, `?`). **This should be used most of the time in this course.**
*   `-i`: Perform a case-insensitive match.
*   `-v`: Invert the match, printing only lines that do *not* match the pattern.
*   `-c`: Print only a count of matching lines, not the lines themselves.
*   `-w`: Match the pattern only if it forms a whole word. This is crucial to avoid matching substrings inside other words (e.g., matching "cat" in "education").
*   `-x`: Match the pattern only if it matches the entire line.
*   `--color=auto`: Highlights the matching part of the string in the output, which is very useful for debugging.

*   **Slide Cross-reference:** grep: select lines matching a pattern (Slide 24/62).

**3.2.3. Flavours of `grep`**
*   `grep -F` or `fgrep`: Matches fixed strings only, not regular expressions. It is faster and safer if the search string might contain regex special characters.
*   `grep -G` (default `grep`): A legacy mode that supports only a basic subset of regular expressions. It exists for backward compatibility.
*   `grep -E` or `egrep`: The modern standard, supporting POSIX extended regular expressions. This is the recommended version for this course.
*   `grep -P`: Supports Perl-compatible regular expressions (PCRE), which include additional features beyond the POSIX standard.

*   **Slide Cross-reference:** grep and friends (Slide 25/62).

#### **3.3. Example: `fgrep` Implementation**
The lecture provided `fgrep.c` and `fgrep.py` as simplified implementations of a line-selection filter. These programs take a substring as the first argument and file paths as subsequent arguments, printing any line from the files that contains the substring, prefixed with the filename and line number. These serve as a conceptual bridge to the more powerful `grep`.

*   **Slide Cross-reference:** selecting lines containing a string - C (Slide 14/62), selecting lines containing a string - Python (Slide 16/62).

---
### **Part IV: Foundational Filters for Data Manipulation**

This section covers a suite of fundamental Unix filters, each designed for a specific data manipulation task.

#### **4.0. `wc` (Word Count)**
The `wc` command summarizes its input by counting lines, words, and characters (or bytes).
*   **Options:**
    *   `-l`: Print only the line count.
    *   `-w`: Print only the word count.
    *   `-c`: Print only the byte count.
    *   `-m`: Print the character count (important for multi-byte Unicode).
*   **Definition of a Word:** In this context, a word is a maximal sequence of non-space characters.
*   **Slide Cross-reference:** wc: word counter (Slide 26/62), wc in C (Slide 27/62), wc in Python (Slide 28/62).

#### **4.1. `tr` (Transliterate)**
The `tr` command performs character-by-character translation or deletion on a stream. It is byte-based and does not accept filenames, reading only from `stdin`.
*   **Usage:** `tr 'source_chars' 'dest_chars'`
*   **Key Use Cases:**
    1.  **Case Conversion:** `tr 'a-z' 'A-Z'` converts input to uppercase.
    2.  **Deleting Characters:** `tr -d '0-9'` deletes all digits.
    3.  **Squeezing Characters:** `tr -s ' '` squeezes multiple spaces into one.
    4.  **Tokenizing:** `tr -cs 'a-zA-Z0-9' '\n'` replaces any character that is not alphanumeric with a newline, effectively putting each word on its own line. This is a very powerful technique for preparing text for word-based analysis.
*   **Slide Cross-reference:** tr: transliterate characters (Slides 29/62, 30/62, 31/62).

#### **4.2. `head` and `tail`**
These filters select the first or last lines of their input.
*   `head`: Prints the first *n* lines (default 10).
*   `tail`: Prints the last *n* lines (default 10).
*   **Option:** `-n <number>` (or just `-<number>`) specifies the number of lines.
*   **Use Case:** Excellent for inspecting the beginning or end of large files or pipeline outputs without displaying the entire content.
*   **Slide Cross-reference:** head/tail: select first/last lines (Slide 32/62).

#### **4.3. Delimited Data**
Many datasets are structured into columns separated by a special character (a delimiter), such as a tab, comma (CSV), or pipe (`|`). Many filters are designed to work with this format.

*   **Slide Cross-reference:** Delimited Input (Slides 33/62, 34/62).

#### **4.4. `cut` (Vertical Slice)**
The `cut` command extracts vertical sections (columns or character positions) from its input.
*   **Options:**
    *   `-f <list>`: Selects fields (columns).
    *   `-c <list>`: Selects character positions.
    *   `-d '<char>'`: Specifies the field delimiter. The default is tab.
*   **Caveat:** The shell may interpret the delimiter character specially, so it often needs to be quoted (e.g., `cut -d'|' ...`).
*   **Slide Cross-reference:** cut: vertical slice (Slides 35/62, 36/62).

#### **4.5. `sort`**
The `sort` command arranges lines of text in a specified order.
*   **Options:**
    *   `-r`: Reverse the sort order (descending).
    *   `-n`: Perform a numeric sort instead of a lexicographical (dictionary) sort. This is essential for correctly sorting numbers (e.g., 9 comes before 45).
    *   `-t '<char>'`: Specifies the field delimiter for column-based sorting.
    *   `-k <n>`: Sorts based on the *n*-th column.
*   **Caveat:** The option for specifying a delimiter (`-t`) is different from `cut`'s (`-d`), a historical inconsistency.
*   **Slide Cross-reference:** sort: sort lines (Slides 37/62, 38/62, 39/62), sort in Python (Slide 40/62).

#### **4.6. `uniq` (Unique)**
The `uniq` command filters out adjacent, identical lines.
*   **Key Pattern:** Because it only works on *adjacent* lines, `uniq` is almost always preceded by `sort` in a pipeline. The `sort | uniq` combination is a fundamental pattern for finding the unique lines in a file.
*   **Options:**
    *   `-c`: The most powerful option. It prefixes each unique line with a count of how many times it occurred. `sort | uniq -c` is a standard idiom for creating frequency counts.
    *   `-d`: Print only duplicated lines.
    *   `-u`: Print only unique (non-duplicated) lines.
*   **Slide Cross-reference:** uniq: remove or count duplicates (Slide 41/62), uniq in C (Slide 42/62), uniq in Python (Slide 43/62).

---

### **Part V: Advanced Filters and Shell Scripting**

#### **5.0. `sed` (Stream Editor)**
`sed` is a powerful, non-interactive editor for streams. It processes input line by line, applying editing commands.
*   **Core Commands:**
    *   `s/regex/replace/g`: The substitute command is its most common use, replacing all occurrences (`g` flag) of a regex with a replacement string.
    *   `d`: Delete lines matching a pattern.
    *   `p`: Print lines matching a pattern.
*   **Options:**
    *   `-n`: Suppress default output; only print lines explicitly told to with the `p` command.
    *   `-E`: Use extended regular expressions.
    *   `-i`: Edit a file "in-place" (safely handles the read/write problem).
*   **Slide Cross-reference:** sed: stream editor (Slides 44/62 through 50/62).

#### **5.1. `find` (File Search)**
The `find` command searches directory trees for files matching specified criteria (name, type, modification time, etc.) and performs actions on them.
*   **Usage:** `find <path> <tests> <actions>`
*   **Examples:**
    *   `find . -name '*.html'`: Find all files ending in `.html` in the current directory and its subdirectories.
    *   `find . -type f -mtime -2`: Find all files modified in the last 2 days.
    *   `find . -name '*.c' -exec grep -H 'main' {} \;`: For every C file found, execute `grep` to find the main function.
*   **Slide Cross-reference:** find: search for files (Slides 51/62, 52/62, 53/62).

#### **5.2. Introduction to Shell Scripting**

**5.2.1. Shebang (`#!`) and Execution Permissions (`chmod`)**
*   **Shebang:** A file starting with `#!` (e.g., `#!/bin/sh`) is a script. The operating system uses the path following the shebang as the interpreter to run the script's contents.
*   **Permissions:** A script file must have "execute" permission to be run directly. This is set using the `chmod` command.
    *   `chmod u+x script.sh`: Gives the user (owner) execute permission.
    *   `chmod 755 script.sh`: A common setting (`rwxr-xr-x`).

**5.2.2. Exit Status and Conditional Logic (`if`, `while`)**
The shell's control flow structures are built around the concept of command success or failure.
*   **Exit Status:** Every command, upon termination, returns an integer exit status to its parent process. By convention:
    *   `0`: Success.
    *   Non-zero (typically `1`): Failure.
*   **`$?` Variable:** The special shell variable `$?` holds the exit status of the most recently executed command.
*   **`if` and `while`:** These shell constructs do not evaluate a boolean expression directly. Instead, they execute a command and branch based on its exit status. If the exit status is `0`, the condition is considered "true."
    *   `if command; then ...; fi`
    *   `while command; do ...; done`
*   **`true` and `false`:** These are actual commands that do nothing but exit with status `0` and `1` respectively, allowing for infinite loops (`while true`) or simple branching.

**5.2.3. Shell Variables and Arguments**
*   **Arguments:**
    *   `$1`, `$2`, ...: The first, second, etc., command-line arguments.
    *   `$@`: All command-line arguments, treated as separate words. `"$@"` is the safe way to pass all arguments to another command.
    *   `$#`: The number of command-line arguments.
    *   `$0`: The name of the script itself.
*   **Best Practice:** Assign positional parameters to named variables early in a script for readability (e.g., `url="$1"`).

**5.2.4. The `test` command (`[]`)**
The `test` command is a standard utility that evaluates an expression and exits with status `0` (true) or `1` (false). It does not produce output. It is the primary tool for comparisons in shell scripts.
*   **Syntactic Sugar:** The `[` command is an alias for `test`. When using it, the final argument must be a `]`.
    *   `test "$#" -eq 1` is equivalent to `[ "$#" -eq 1 ]`.
*   **Caveat:** Spaces around the `[` and `]` are mandatory and a common source of errors.
*   **Expressions:**
    *   String comparison: `=`, `!=`
    *   Integer comparison: `-eq`, `-ne`, `-gt`, `-lt`, `-ge`, `-le`
    *   File tests: `-f` (is file), `-d` (is directory)

**5.2.5. Scripting Best Practices and Debugging**
*   **Comments:** Use comments (`#`) to explain the purpose and logic of your scripts.
*   **Layout:** Break long pipelines across multiple lines for readability.
*   **Error Handling:**
    1.  Check the number of arguments (`$#`).
    2.  Print a helpful `Usage:` message to standard error (`>&2`).
    3.  Exit with a non-zero status (`exit 1`) on error.
*   **Debugging:**
    *   `set -x`: A shell option that prints each command before it is executed. Can be added to the top of a script or used when running it (`sh -x script.sh`).
    *   `echo`: Print the values of variables at key points.
    *   Incremental Development: Build and test pipelines and scripts piece by piece.

#### **5.3. Web Scraping with `curl` and `wget`**
These are command-line tools for fetching content from URLs.
*   `wget`: By default, saves content to a file. Use `-O -` to print to `stdout`.
*   `curl`: By default, prints content to `stdout`.
*   **Options:** Both have "silent" or "quiet" modes (`curl -s`, `wget -q`) to suppress progress meters, which is essential for scripting.
*   **Use Case:** These commands are the entry point for bringing web data into a shell pipeline for processing with tools like `grep`, `sed`, and `cut`.

**Example: Website Watcher Script**
The lecture developed a script to periodically fetch a webpage, check it for a pattern, and take an action.
*   **Rate Limiting:** A `sleep` command inside the loop is critical to avoid overwhelming the web server (a denial-of-service risk) and getting blocked.
*   **Local Testing:** For development, it is common to run a simple local web server (e.g., with `python3 -m http.server`) to test the script without hitting a live production server.

#### **5.4. Advanced Filters**
*   `join`: Performs a database-style join operation on two sorted files based on a common key field.
*   `paste`: Merges files line-by-line, creating columns.
*   `tee`: Splits a stream, sending it to both `stdout` and a file.
*   `xargs`: Builds and executes command lines from standard input.
*   **Process Substitution:** A bash-specific feature `<(command)` that allows the output of a command to be treated like a file, useful for tools that require file arguments instead of `stdin`.

*   **Slide Cross-reference:** join (Slide 54/62), paste (Slide 56/62), tee (Slide 58/62), xargs (Slide 59/62), process substitution (Slide 61/62).