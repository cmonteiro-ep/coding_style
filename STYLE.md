# 🦍 Banana internal coding style 🍌

This document explains all the rules and tools used to standardize the coding style in the `banana-coding-style-checker` project. 

## Tools

The coding style is checked using a linter ([pylint](https://www.pylint.org/)).

You will find the configuration at the root of the repository in the file
`.pylintrc`.

## Rules

You should not add a shebang at the beginning of a rule file.

Use the `path` lib from `os` to manipulate file paths

```python
filename = path.basename(file)  # OK
filename = f.split(os.sep)[-1]  # UGLY
```

When using a library, try to keep only the most significant namespace.

```python
# OK
from os import path

path.basename(file)

# UGLY
from os.path import basename

basename(file)

# UGLY
import os

os.path.basename(file)
```

Globals variables must be in capital SNAKE_CASE.

```python
I_AM_A_GLOBAL = "yes"  # OK
i_am_a_global = "no"  # UGLY
```

Use explicit variables names.

```python
# OK
line_count = 0
file = "main.c"

# UGLY
lc = 0
f = "main.c"
```

All function variables must be in lowercase snake_case.

```python
def main():
    i_am_a_local_variable = "yes"  # OK
    I_AM_A_LOCAL_VARIABLE = "no"  # UGLY
```

When filtering files to test, you must use the functions from the `utils` module:
```python
from utils import is_header_file, is_source_file, is_makefile

for file in vera.getSourceFileNames():
    if not is_source_file(file) and not is_header_file(file) and not is_makefile(file):
        continue
```
You can also get the extension with `get_extension` and the file name with `get_filename` or `get_filename_without_extension`.

Merging all lines into one buffer must be done like that:

```python
raw = '\n'.join(vera.getAllLines(f))
```

As a subsequent rule, all lines must be considered ending with `\n` (as the Epitech's C coding style applies to Unix).

## Question?

Ask a GORILLA.
