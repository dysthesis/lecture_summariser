Here are the comprehensive lecture notes for the COMP(2041|9044) Course Introduction.

***

### **Lecture Notes: Course Introduction, Unix Philosophy, and Regular Expressions**

#### **1.0 Course Overview and Administration**

This lecture provides a comprehensive introduction to the course COMP(2041|9044) Software Construction. It outlines the course's philosophy, learning objectives, administrative structure, assessment scheme, and foundational technical concepts.

##### **1.1 Staff and Teaching Team**

*   **Convenor & Lecturer:** Andrew Taylor
*   **Administration:** Dylan Brotherston, Anna Brew
*   **Tutors:** A large team of past students has been recruited to facilitate tutorials and labs. They will also be active on the course forum.

##### **1.2 Course Goals and Philosophy**

This course aims to bridge the gap between foundational programming skills and the practical demands of real-world software development. While introductory programming courses (e.g., COMP1511, COMP9021) typically focus on a single language (C or Python), small, well-defined problems, and narrow programming aspects, COMP(2041|9044) broadens this scope significantly.

**Key Learning Objectives:**
*   **Multi-language Proficiency:** Gain proficiency in other languages, specifically Shell and Python, beyond the initial language learned.
*   **Software Composition:** Learn to combine multiple programs and tools to solve complex problems, a core tenet of the Unix philosophy.
*   **Problem Specification:** Tackle larger, less-specified problems that require more analysis and design.
*   **Development Tools:** Master essential software development tools such as `git` for version control and `docker` for containerisation.
*   **System Configuration:** Understand and perform system configuration tasks, including using package managers and mounting file systems.

The ultimate practical goal is to equip students with the skills necessary to build a software package, host it on a platform like GitHub, and enable others to download and use it. In essence, the course seeks to expand students' software building capabilities.

**Slide Cross-reference:** 3, 4

##### **1.3 Assumed Knowledge**

Students are expected to possess the following prerequisite skills:
*   The ability to write, debug, and test programs in either C or Python.
    *   Knowledge of C is not strictly essential; the course depends very little on it.
    *   Basic Python knowledge is assumed. Students without any Python background are strongly encouraged to undertake introductory self-study in the first few weeks of the term, as the course will not cover Python fundamentals from scratch. Resources are abundant online, and the course forum is available for recommendations.
*   An appreciation for the use of abstraction in computing.

**Slide Cross-reference:** 5

##### **1.4 Recent Course Changes**

For students familiar with previous iterations of the course or online discussions, several key changes have been implemented:
*   **Web Development:** Web frontend/backend programming is no longer part of this course. This content has been moved to COMP6080. The course will, however, cover scripting for scraping and downloading web data.
*   **Perl Replacement:** The Perl programming language has been replaced with Python. Python has largely supplanted Perl in the domains relevant to this course.

**Slide Cross-reference:** 6

---

#### **2.0 Course Mechanics and Structure**

##### **2.1 Lectures**

*   **Schedule:** Mondays, 14:00–16:00 (in-person) and Thursdays, 14:00–16:00 (online).
*   **Format:**
    *   Monday lectures are delivered in person and recorded via Echo360.
    *   Thursday lectures are live-streamed via YouTube. Students are encouraged to participate by asking questions in the live chat.
*   **Recordings:** All lectures are recorded and links are made available on the course homepage.
*   **Content Style:** Lectures will present a brief overview of theory but will focus heavily on practical demonstrations of coding, testing, and debugging to illustrate problem-solving processes.
*   **Slides:** Lecture slides will be available on the course website prior to each lecture.

**Slide Cross-reference:** 7

##### **2.2 Tutorials and Lab Classes**

*   **Schedule:** Tutorials commence in Week 1 and run weekly, except for Flex-Week (Week 6). They are one-hour sessions followed by a two-hour lab class.
*   **Purpose of Tutorials:**
    *   Clarify concepts from lectures.
    *   Work through related problems to prepare for labs and assignments.
    *   Provide practice in design and problem-solving.
*   **Maximising Tutorial Value:** Students are encouraged to attempt tutorial problems beforehand and actively participate in discussions. Tutors are instructed to facilitate an interactive environment rather than deliver a mini-lecture.
*   **Lab Classes:**
    *   Labs consist of several small, individual implementation and analysis tasks.
    *   They aim to build skills necessary for assignments and the final exam.
    *   **Submission:** Labs are submitted via the `give` command before 12:00 (midday) on the Monday of the following week.
    *   **Marking:** Labs are automarked and contribute 15% to the final grade.
    *   **Challenge Exercises:** Labs may include optional challenge exercises that can be difficult or unconventional. It is possible to achieve 95% of the lab marks without completing any challenge exercises.

**Slide Cross-reference:** 8, 9

##### **2.3 Weekly Tests**

*   **Schedule:** Starting from Week 3, there will be 8 weekly programming tests.
*   **Format:** These are conducted in the student's own time under self-enforced exam conditions, with a time limit of 1 hour.
*   **Marking:** Tests are automarked. The best 6 of 8 test results will contribute 10% to the final mark. Submissions after the 1-hour mark receive a half-mark penalty.
*   **Integrity:** Any violation of the test conditions will result in a mark of zero for the entire component.

**Slide Cross-reference:** 10

##### **2.4 Assignments**

*   **Structure:** There will be two major individual assignments.
    *   **Assignment 1:** Due Monday of Week 7.
    *   **Assignment 2:** Due Monday of Week 11.
*   **Nature:** Assignments involve applying course concepts to larger, more complex programming problems than those found in labs.
*   **Advice:** It is strongly advised to start assignments early, as they invariably take longer than anticipated. Help sessions will be available but become overwhelmed close to the deadline.

**Slide Cross-reference:** 11

##### **2.5 Late Penalties and Marking Timelines**

*   **Late Penalty:** A standard UNSW late penalty applies to all assessable items (Labs, Tests, Assignments). A deduction of 0.2% of the raw mark is applied for each hour an item is late. After 5 days (120 hours), a 100% penalty is applied.
    *   *Example:* A raw mark of 80/100 submitted 1 minute late (rounded to 1 hour) becomes 79.8/100.
    *   *Example:* A raw mark of 78/100 submitted 3 days, 8 hours, and 42 minutes late (rounded to 81 hours) becomes 61.8/100.
*   **Solution and Mark Release:** Due to the 5-day late submission window and potential special consideration extensions, sample solutions and marks for labs and tests will be released approximately two weeks after the due date. Sample solutions for assignments are not released. Assignment marks are released in two stages: automarking results after two weeks, and hand-marking results approximately two weeks after that.

**Slide Cross-reference:** 12, 13

##### **2.6 Code of Conduct and Academic Integrity**

*   **Conduct:** All students are expected to maintain a respectful and inclusive environment in all course-related interactions. Misconduct, including racist, sexist, or offensive language, bullying, and harassment, will not be tolerated. Students are reminded to treat interactions with staff and peers as they would in a professional workplace.
*   **Plagiarism:** All submitted work (labs, tests, assignments) must be entirely the student's own.
    *   **Prohibited Actions:** Group work on individual assignments, reading another student's code before starting, allowing another student to copy your work, and purchasing solutions are all forms of academic misconduct.
    *   **Consequences:** Plagiarism is checked for electronically and carries severe penalties, which can include suspension from UNSW, loss of scholarships, and visa cancellation for international students. Supplying work to others can result in a loss of all marks for that assessment item.

**Slide Cross-reference:** 14, 15, 16

##### **2.7 Use of Generative AI**

*   **Policy:** The use of generative AI tools such as GitHub Copilot and ChatGPT is **not permitted** in COMP(2041|9044) for most assessments, including labs, tests, and the final exam.
*   **Rationale:** While these tools have potential, their effective and safe use requires a deep understanding of the code they generate. For learners, reliance on these tools can hinder the development of fundamental coding skills and the ability to identify subtle errors and security vulnerabilities often present in generated code.
*   **Assignments Exception:** Assignments may permit the use of a small amount of generated code, but this must be explicitly attributed as per the assignment specification. Students must read each specification carefully.
*   **Exam Context:** Generative AI will not be available during the final exam, making it essential to develop proficiency without these aids.

**Slide Cross-reference:** 17

##### **2.8 Final Exam and Overall Assessment**

*   **Final Exam (45%):**
    *   An in-person, practical programming exam conducted in CSE labs during the official exam period.
    *   It is a closed-book exam, though limited language documentation will be available.
    *   The format includes multiple-choice/short-answer questions and 8-12 implementation tasks similar to lab exercises, primarily in Shell and Python.
    *   **Hurdle Requirement:** Students **must score at least 18/45 (40%) on the final exam** to be eligible to pass the course, regardless of their overall mark.
*   **Assessment Breakdown:**
    *   Labs: 15%
    *   Weekly Tests: 10%
    *   Assignment 1: 15%
    *   Assignment 2: 15%
    *   Final Exam: 45%
*   **Passing Conditions:** To pass the course, a student must achieve both:
    1.  An overall mark of 50/100 or higher.
    2.  A final exam mark of 18/45 or higher.

**Slide Cross-reference:** 18, 19

---

#### **3.0 Technical Content: Unix Filters and Regular Expressions**

##### **3.1 The Unix Philosophy: Byte Streams and Filters**

A foundational concept in Unix-like systems is the use of small, single-purpose programs called **filters**.

*   **Definition of a Unix Filter:** A program that reads data from a source (typically standard input), performs a transformation on that data, and writes the result to a destination (typically standard output).
*   **Byte Streams:** When a program starts, it is connected to three standard I/O streams:
    1.  `stdin`: Standard input, the default source of data.
    2.  `stdout`: Standard output, the default destination for results.
    3.  `stderr`: Standard error, a separate stream for error messages.
*   **Data as Bytes:** The data in these streams consists of bytes. A byte is an 8-bit value (0-255). Its meaning is determined by interpretation. In this course, bytes are almost always interpreted as text.
*   **Text Encoding:**
    *   **ASCII (American Standard Code for Information Interchange):** A 7-bit code (128 characters) sufficient for English but inadequate for most other world languages.
    *   **UTF-8:** A variable-width encoding for Unicode, which aims to represent all characters from all languages. It is the de facto standard on the modern web and in most systems. While the course will primarily operate in an ASCII context, awareness of UTF-8 is important for real-world programming.
*   **Pipelines (`|`):** The true power of filters is realised when they are chained together in a **pipeline**. The pipe symbol (`|`) is a shell operator that connects the `stdout` of one program to the `stdin` of the next. This allows for the construction of complex data processing workflows from simple, reusable components.

##### **3.2 Example 1: The `cat` (Concatenate) Filter**

The `cat` command is the "identity filter"—it reads bytes and writes them out unchanged. While seemingly trivial, it serves as an excellent illustration of the standard filter behaviour pattern.

*   **Behaviour Pattern:**
    1.  If invoked with no command-line arguments, read from `stdin`.
    2.  If invoked with one or more arguments, treat each argument as a filename, open each file in sequence, and process its contents.

*   **Example Code: `cat.c`**
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    
    void process_stream(FILE *stream);
    
    int main(int argc, char *argv[]) {
        if (argc == 1) {
            process_stream(stdin);
        } else {
            for (int i = 1; i < argc; i++) {
                FILE *in = fopen(argv[i], "r");
                if (in == NULL) {
                    perror(argv[i]);
                    return 1;
                }
                process_stream(in);
                fclose(in);
            }
        }
        return 0;
    }
    
    // Identity filter: get a byte from stream, send it to stdout
    void process_stream(FILE *stream) {
        int c;
        while ((c = fgetc(stream)) != EOF) {
            fputc(c, stdout);
        }
    }
    ```
*   **Example Code: `cat.py`**
    ```python
    #!/usr/bin/env python3
    
    import sys
    
    def main():
        if len(sys.argv) == 1:
            process_stream(sys.stdin)
        else:
            for path in sys.argv[1:]:
                try:
                    with open(path) as f:
                        process_stream(f)
                except OSError as e:
                    print(f"{sys.argv[0]}: {path}: {e}", file=sys.stderr)
    
    # Python version works line-by-line
    def process_stream(stream):
        for line in stream:
            print(line, end='')
    
    if __name__ == '__main__':
        main()
    ```

*   **Demonstration:**
    ```bash
    # Compiling the C version
    $ gcc cat.c -o my_cat
    
    # Running the compiled C program
    $ ./my_cat
    hello dylan      # Input
    hello dylan      # Output
    ^D               # End of input
    
    # Piping multiple instances together
    $ ./my_cat | ./my_cat | ./my_cat
    hello comp2041   # Input
    hello comp2041   # Output
    ```

##### **3.3 Introduction to Regular Expressions (Regex)**

A **regular expression** is a sequence of characters that specifies a search pattern. More formally, it is a notation for defining a set of strings.

*   **Historical Context:**
    *   **Stephen Kleene:** A mathematician who developed the theoretical foundations in the 1950s.
    *   **Ken Thompson:** A computer scientist who, while developing early Unix tools, adapted Kleene's notation into a practical, ASCII-based syntax and created an efficient implementation. This work was a key part of his Turing Award-winning contributions.
*   **Ubiquity:** Regex is a fundamental tool used in virtually every programming language (Python, JavaScript, C++, Java), text editor, and command-line utility for pattern matching.

**Core Regex Syntax:**

| Metacharacter | Name | Description | Example | Matches |
| :--- | :--- | :--- | :--- | :--- |
| `.` | Dot / Wildcard | Matches any single character (except newline). | `h.t` | `hat`, `hot`, `h_t`, etc. |
| `*` | Asterisk / Kleene Star | Matches the preceding element zero or more times. | `ab*c` | `ac`, `abc`, `abbc`, `abbbc`, etc. |
| `+` | Plus / Kleene Plus | Matches the preceding element one or more times. | `ab+c` | `abc`, `abbc` (but not `ac`). |
| `?` | Question Mark | Matches the preceding element zero or one time (makes it optional). | `colou?r` | `color`, `colour`. |
| `|` | Pipe / Alternation | Acts as an OR operator, matching the expression on its left or right. | `cat\|dog` | `cat`, `dog`. |
| `[]` | Character Set | Matches any single character within the brackets. | `[aeiou]` | `a`, `e`, `i`, `o`, or `u`. |
| `[^]` | Negated Set | Matches any single character **not** within the brackets. | `[^0-9]` | Any non-digit character. |
| `()` | Grouping | Groups sub-expressions, allowing operators to apply to the whole group. | `(ab)+` | `ab`, `abab`, `ababab`, etc. |
| `^` | Caret / Start Anchor | Matches the start of a line. | `^The` | A line beginning with "The". |
| `$` | Dollar / End Anchor | Matches the end of a line. | `end$` | A line ending with "end". |
| `{n,m}` | Quantifier | Matches the preceding element a specific number of times. `{n}` (exactly n), `{n,}` (n or more), `{n,m}` (between n and m). | `z[0-9]{7}` | `z` followed by exactly 7 digits (e.g., a UNSW student ID). |
| `\` | Backslash / Escape | Removes the special meaning of the following metacharacter. | `\.\*` | The literal characters `.` and `*`. |

*   **Caveat:** Mastering regex requires practice. Online tools like **`regex101.com`** and **`regexr.com`** are highly recommended for interactively building and debugging regular expressions.

##### **3.4 The `grep` Command**

`grep` (Global Regular Expression Print) is a quintessential Unix utility that searches for lines matching a regular expression.

*   **Basic Usage:** `grep [OPTIONS] PATTERN [FILE...]`

*   **Key Options and Examples:**
    *   `-E` (Extended Regex): **Crucial for this course.** Unlocks the full power of regex, including `|`, `+`, `?`, and `{}`. This is needed for historical reasons; modern systems are fast enough that it should be the default, but it remains an option for backward compatibility. **It is recommended to use `-E` for all `grep` commands in this course.**
        ```bash
        # Find courses mentioning 'computer' OR 'software' (case-sensitive)
        $ grep -E 'computer|software' course_codes.txt 
        ```
    *   `-i` (Ignore Case): Performs case-insensitive matching.
        ```bash
        # Find courses mentioning 'computer' regardless of case
        $ grep -i 'computer' course_codes.txt
        ```
    *   `-v` (Invert Match): Selects lines that **do not** match the pattern.
        ```bash
        # Show all lines EXCEPT those containing 'Dylan'
        $ grep -v 'Dylan'
        ```
    *   `-w` (Whole Word): Matches the pattern only if it forms a whole word (bounded by non-word characters). This prevents unwanted partial matches.
        ```bash
        # Search for the word 'cat', not as a substring in 'caterpillar'
        $ grep -w 'cat' courses.txt
        ```
    *   `-c` (Count): Suppresses normal output and instead prints a count of matching lines.
        ```bash
        # Count how many courses are about 'cats'
        $ grep -c -w 'cat' courses.txt
        ```
    *   `--color=auto`: Highlights the matching text, which is extremely useful for debugging patterns.
    *   `-x` (Whole Line): The pattern must match the entire line.
    *   `-f FILE`: Read patterns from `FILE`, one per line.
    *   `-P` (Perl-compatible): Enables an even richer set of regex features, which will be discussed later in the course.

*   **Practical Advice:**
    *   **Quoting:** Always enclose your regular expression in single quotes (`'...'`) on the command line. This prevents the shell from interpreting special characters like `*`, `|`, and `$` before `grep` sees them.
    *   **Case Sensitivity:** When performing string matches, always consciously decide if the match should be case-sensitive or case-insensitive (`-i`). This is a common source of bugs.
    *   **Substring vs. Whole Word:** Be aware of whether a substring match is sufficient or if a whole-word match (`-w`) is required to avoid false positives.