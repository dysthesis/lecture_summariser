Of course. Here are the comprehensive lecture notes from the provided materials.

***

### **Lecture 9: Git Internals**

These notes provide a comprehensive summary of the lecture on the internal workings of the Git version control system. The lecture focuses on deconstructing the `.git` directory to understand how Git stores data and manages version history through its core components: objects, the index, and references.

### **1. The Anatomy of a `.git` Repository**

When a new Git repository is created via `git init`, it populates a hidden `.git` directory with a standard file and directory structure. While several components exist, the lecture focuses on four core elements essential for understanding Git's functionality.

**Key Concepts:**

*   **Initial Structure:** A fresh `.git` directory contains several items, including `config`, `description`, `HEAD`, `hooks`, `info`, `objects`, and `refs`.
*   **Core Components:** For this lecture's purpose, the critical components are narrowed down to:
    1.  `config`: A file containing repository-specific configuration.
    2.  `HEAD`: A file that acts as a pointer to the current location in the repository's history.
    3.  `objects`: A directory that serves as the database for all content and metadata.
    4.  `refs`: A directory containing pointers (references) to specific commits, such as branches and tags.
*   **Auxiliary Components:** Other components, such as `hooks` (for custom scripts), `info` (for metadata), `description` (for GitWeb), and the deprecated `branches` directory, are not central to the core mechanics discussed and were excluded from the detailed analysis.

**Slide Cross-reference:** Slides 8 and 9 illustrate the file structure of a `.git` repository, both in its initial state and after several commits and branches have been created.

#### **1.1. The `config` File**

The `.git/config` file stores settings specific to the repository. The lecture highlights several default key-value pairs:
*   `repositoryformatversion = 0`: This has been the standard version for a long time and is unlikely to change.
*   `filemode = true`: This setting instructs Git to track execute permissions on files, which is relevant for UNIX-like systems such as Linux. It can be set to `false` on systems like Windows that do not handle file permissions in a compatible way.
*   `bare = false`: This indicates that the repository is a standard working repository, containing both the `.git` directory (metadata) and the working tree (the actual files). A "bare" repository, often used for hosting on servers like GitHub, contains only the `.git` directory contents.
*   `logallrefupdates = true`: This enables more detailed logging of changes to references, which can be useful for diagnostics.

#### **1.2. The `HEAD` File**

The `HEAD` file is a symbolic reference that points to the current branch or commit. In a new repository, it typically contains a single line pointing to the default branch (e.g., `main` or `master`):

```
ref: refs/heads/main
```

This indicates that `HEAD` is pointing to the `main` branch, which is located at the file path `.git/refs/heads/main`. The name of the current branch is derived from this file.

### **2. Git's Core Data Structures: The Object Database**

Git operates as a content-addressable filesystem. All data—file content, directory structures, and commit metadata—is stored as objects within the `.git/objects` directory. There are three primary types of objects: blobs, trees, and commits.

**Key Concept:** Every object is identified by a unique 40-character SHA-1 hash of its content. This hash is used as the object's "name" in the object database. For storage efficiency, the first two characters of the hash are used as a directory name, and the remaining 38 characters form the filename (e.g., an object with hash `0eacb5...` is stored at `.git/objects/0e/acb5...`).

**Slide Cross-reference:** Slide 7 provides a concise definition of Blobs, Trees, and Commits. Slide 11 explains the SHA-1 hashing and directory structure for storing objects.

#### **2.1. Blob Objects: Storing File Content**

A **blob** (Binary Large Object) stores the raw content of a file. It contains no metadata, such as the filename or permissions.

**Key Concepts:**
*   **Structure:** A blob object's content is composed of a header and the file's data. The header consists of the word `blob`, a space, the size of the content in bytes, a null byte (`\0`), and then the raw file content itself.
*   **Example Format:** `blob 12\0dylanb is 42`
*   **Compression:** The complete object content (header + data) is compressed using Zlib (specifically, at compression level 1 as determined by reverse-engineering the output) before being stored in the `.git/objects` directory.
*   **Identification:** The SHA-1 hash of the uncompressed object content (e.g., `sha1sum("blob 12\0dylanb is 42")`) determines the object's filename.

**Example: Manually Creating a Blob**
The lecture demonstrated how to manually recreate a blob object for a file named `numbers` containing `dylanb is 42` (12 bytes).

1.  **Construct the content:** The uncompressed content is created. The null byte is critical.
    ```bash
    # Note: echo needs the -e flag to interpret backslash escapes like \0
    # and -n to avoid a trailing newline.
    (echo -en "blob 12\0"; cat numbers)
    ```
2.  **Generate the SHA-1 Hash:** This content is piped to `sha1sum` to get the object's ID.
    ```bash
    (echo -en "blob 12\0"; cat numbers) | sha1sum
    # Output: 0eacb5ee5417438577f200a1323959c79c6bcbebd98b52f95c -
    ```
3.  **Compress the content:** The content is compressed using `pigs` (a parallel implementation of `gzip`) with Zlib format and level 1 compression.
    ```bash
    # The output of this command is the final binary content for the object file.
    (echo -en "blob 12\0"; cat numbers) | pigs -z -c -1
    ```

#### **2.2. The Index: The Staging Area**

When a file is staged using `git add`, Git creates a corresponding blob object and records it in a special file called the **index** (located at `.git/index`). The index acts as a staging area, holding a snapshot of the files that will be included in the *next* commit.

**Key Concepts:**
*   **Function:** The index maps file paths to blob object hashes. It bridges the gap between the file-agnostic blob objects and the file names in the working directory.
*   **Format:** The index is a binary file. Its contents can be inspected with the command `git ls-files -s`.
*   **Structure of an Entry:** Each line in the output of `git ls-files -s` represents an entry in the index and has the following format: `[mode] [hash] [stage] [file path]`
    *   `mode`: The file permissions (e.g., `100644` for a regular file).
    *   `hash`: The SHA-1 hash of the corresponding blob object.
    *   `stage`: A number related to merge status. It is `0` for normal files. During a merge conflict, multiple entries for the same file path can exist with different stage numbers (1 for the common ancestor, 2 for "our" version, and 3 for "their" version).
    *   `file path`: The full path to the file from the repository root (e.g., `numbers` or `number/big`).

**Caveat: Index vs. Tree Structure:** The index stores a flat list of all file paths in the repository. This is distinct from the hierarchical structure of tree objects.

#### **2.3. Tree Objects: Storing Directory Structure**

A **tree** object represents a directory in the filesystem. It contains a list of entries, where each entry points to either a blob (for a file) or another tree (for a subdirectory).

**Key Concepts:**
*   **Function:** A tree object maps file and directory names to their corresponding blob or tree objects, along with their permissions.
*   **Structure of an Entry:** When inspected with `git cat-file -p <hash>`, a tree object shows a list of entries with the format: `[mode] [type] [hash] [name]`
    *   `mode`: File or directory permissions.
    *   `type`: The type of the referenced object (`blob` or `tree`).
    *   `hash`: The SHA-1 hash of the referenced blob or tree.
    *   `name`: The basename of the file or directory (not the full path).
*   **Hierarchical Nature:** Subdirectories are represented by a tree object pointing to other tree objects, creating a recursive structure that mirrors the filesystem. If a file within a commit does not change, the new tree object can simply point to the pre-existing blob, saving storage space.

#### **2.4. Commit Objects: Snapshots in Time**

A **commit** object represents a snapshot of the entire repository at a specific moment in time. It ties together the directory structure, metadata, and historical lineage.

**Key Concepts:**
*   **Function:** A commit acts as a historical marker, capturing the state of the project, who made the changes, when they were made, and why.
*   **Structure:** A commit object, inspected with `git cat-file -p <hash>`, contains the following information:
    *   `tree <hash>`: A pointer to the root tree object that represents the state of the working directory for this commit.
    *   `parent <hash>`: A pointer to the preceding commit(s). The first commit (root commit) has no parent. A regular commit has one parent. A merge commit has two or more parents. This parent-child linkage forms the commit history.
    *   `author <name> <email> <timestamp> <timezone>`: Information about the original author of the changes.
    *   `committer <name> <email> <timestamp> <timezone>`: Information about the person who created the commit. This can differ from the author, for instance when a patch is applied by a maintainer.
    *   A blank line followed by the commit message.

### **3. References (`refs`): Human-Readable Pointers**

Since remembering 40-character SHA-1 hashes is impractical, Git uses **references** (or `refs`) as human-readable pointers to commits. These are stored in the `.git/refs` directory.

**Slide Cross-reference:** Slide 10 describes the role of `HEAD` and the different `refs` directories for branches, tags, and remotes.

#### **3.1. Branches**

Branches are dynamic pointers that move forward automatically as new commits are made. A branch is essentially a file whose name is the branch name (e.g., `.git/refs/heads/main`) and whose content is the SHA-1 hash of the latest commit on that branch.

*   **Branch Creation:** Creating a branch (e.g., `git switch -c colors`) creates a new file at `.git/refs/heads/colors`, containing the hash of the current commit.
*   **Divergent History:** When commits are made on different branches, their respective ref files are updated independently, causing their histories to diverge from a common ancestor. This enables parallel development.

#### **3.2. Tags**

Tags are static pointers to specific commits. They are typically used to mark important historical points, such as software releases (e.g., `v1.0`).

*   **Implementation:** A simple tag is a file whose name is the tag name (e.g., `.git/refs/tags/v1.0`) and whose content is the SHA-1 hash of the commit it points to.
*   **Static Nature:** Unlike branches, tags do not move automatically when new commits are created. They remain fixed on a specific commit.

### **4. Git Operations and Their Internal Effects**

The lecture demonstrated how common Git commands manipulate these internal structures.

*   `git add <file>`: Creates a new blob object for the file's content (if it doesn't already exist) and adds or updates its entry in the `.git/index` file.
*   `git commit`:
    1.  Creates one or more tree objects based on the current state of the index.
    2.  Creates a commit object that points to the root tree and the current parent commit.
    3.  Updates the current branch's ref file (e.g., `.git/refs/heads/main`) to point to the new commit's hash.
*   `git switch <commit|branch|tag>`: Modifies the `.git/HEAD` file to point to the specified location and updates the files in the working directory to match the state of that commit's tree. If switching to a specific commit hash, this results in a "detached HEAD" state, where `HEAD` contains the hash directly instead of a reference to a branch.
*   `git merge <branch>`: When merging divergent branches, Git creates a new **merge commit**. This special commit has two parents, linking the histories of both branches back together. If Git cannot automatically combine changes to the same file, a **merge conflict** occurs, which must be resolved manually by the user before the merge can be finalized.

### **5. Efficiency in Large Repositories: Packed Objects and Refs**

For large repositories with many thousands of objects and references, storing each as an individual file is inefficient in terms of both disk space (due to filesystem overhead) and network transfer.

**Key Concept:** Git periodically "packs" these individual files into a single large file.
*   **Packed Objects:** Multiple object files are compressed and stored in a `.pack` file, with a corresponding `.idx` file for efficient lookup. This is seen in large repositories like the `postgres` or `git` source code. The command `git unpack-objects` can be used to reverse this process for inspection.
*   **Packed Refs:** Similarly, multiple ref files can be combined into a single text file named `packed-refs`. The lecture provided a shell command pipeline to demonstrate how this file could be unpacked back into individual ref files.

### **6. Commands for Internal Inspection**

The lecture made extensive use of several commands to peer inside the `.git` directory and understand its contents.

*   `tree .git`: To visualize the directory structure.
*   `file <path>`: To identify the type of a file (e.g., Zlib compressed data, Git index).
*   `hexdump -C <path>`: To view the raw byte content of a file.
*   `pigs -d -z -c <path>` or `zlib-flate -uncompress < <path>`: To decompress Zlib-compressed object files.
*   `sha1sum <path>`: To calculate the SHA-1 hash of a file's content.
*   `git ls-files -s`: To display the contents of the index.
*   `git cat-file -t <hash>`: To show the type of an object (blob, tree, commit).
*   `git cat-file -p <hash>`: To "pretty-print" the content of an object.
*   `git cat-file -s <hash>`: To show the size of an object.