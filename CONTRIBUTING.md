# Contributing to Banana

In this document are enumerated the different guidelines related to the contribution to Banana 🍌.

## Continuous integration

A Jenkins instance is monitoring the repository and is continuously asserting that the features of Banana are working, and that its code is still at the desired quality.
Pull requests cannot be merged if the CI pipeline is failed.

## Repository structure
### `Jenkinsfile`
File defining the steps taken during the continuous integration process. This file should not be changed.

### `tests`
Directory containing all the files related to Banana's testing (all the information about this is contained in its own [README.md](tests/README.md) file).

### `vera`
Directory containing the proper vera++ rules and profile used to enforce the Epitech's C coding style.

#### `vera/profiles`
Directory containing an `epitech` file, which contains the list of all the enforced rules.
It looks like this:
```tcl
#!/usr/bin/tclsh
# This profile includes all the rules provided by our coding style

set rules {
    C3
    G1
    G2
    G6
    H2
    O1
    O4
}
```
Any rule that is not present here will not be enforced.

Rules should be listed in alphabetical order.

#### `vera/rules`
Directory containing the vera++ rules. Each one takes the form of a Python file bearing the name of the rule (e.g.: `C3.py`, `G1.py`, `H2.py`).

Each rules checks if any violations exist, and reports them if necessary.

#### `vera/code_to_comment`
Text file containing a mapping of each rule's name to its textual description. Said descriptions are used in the students' traces to inform them of what their violations are.

Each mapping is done in the following way: `rule_name:textual description`

Example: `L1:multiple statements on the same line`

Textual descriptions should start with a lowercase letter and be ordered in alphabetical order (with the implicit rules being separated from the other rules).

## Adding a rule to Banana
When adding a rule to Banana, the following steps should be followed:

1. Create a new branch named `XX_rule` from the `develop` branch, with `XX` being the rule's name.
2. Create a Python file with the rule's name in the `vera/rules` directory.
3. Add the rule to the `vera/profiles/epitech` file.
4. Ensure that a textual description for the rule exists in the `vera/code_to_comment` file, otherwise add one.
5. Add comprehensive [tests](tests/README.md) for the rule.
6. Write the rule (please respect the [internal coding style](STYLE.md) while doing so).
7. When all the tests pass (with Jenkins), open a pull request named `XX rule` (with with `XX` being the rule's name) aimed at being merged into `develop`, and request a review from at least one GORILLA 🦍 (the more the better).
8. Iterate on the reviews and requests made.
9. When everything is OK and approved, your PR will be squashed and merged into `develop`.
10. Congratulations, you have now added a rule to Banana!
