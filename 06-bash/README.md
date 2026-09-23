# 06 — Bash Scripting

## Objective

Move from manually typing individual commands to automating workflows systematically:

> *"If I repeatedly perform the same task, I should consider whether I can automate it."*

---

## What Problem Were We Solving?
Automating administrative and security tasks, eliminating human error, and scripting repeatable sequences of system interactions.

## Progression of Concepts
* **Variables & Arguments:** `$1`, `$@`, `$#`, environment variables, string assignment
* **User Input:** Interactive prompting via `read`
* **Conditions:** Numeric & string comparisons (`[[ ... ]]`), `if`/`elif`/`else`, `case` statements
* **Loops:** Iterating over files and lists (`for`, `while`)
* **Functions & Modularity:** Reusable routines, localized scope (`local`), exit status codes (`return`, `exit $?`)

---

## Directory Contents

* [`basics/`](./basics/)
  * `variables.sh` — Variable declarations, parameter expansion, and special parameters.
  * `input.sh` — User input handling with validation.
  * `conditions.sh` — Conditionals, comparison operators, and branching logic.
  * `loops.sh` — `for` and `while` loop implementations.
  * `functions.sh` — Reusable functions, return codes, and error trapping.
* [`project/`](./project/) — Applied automation scripts.
