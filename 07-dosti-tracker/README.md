# 07 — Dosti Tracker

## Objective

Build a command-line habit and accountability tracker using Bash.

The purpose is to combine:
```text
variables + input + conditions + loops + functions + files
```
into one useful, production-grade utility.

---

## Command Interface

The script supports both direct CLI subcommands and an interactive menu when invoked without arguments:

```bash
./dosti.sh add <habit>        # Add a new habit
./dosti.sh update <habit>     # Mark a habit as completed for today
./dosti.sh remove <habit>     # Remove an existing habit
./dosti.sh list               # List all tracked habits and streak counts
./dosti.sh vstreak <habit>    # View the current streak for a specific habit
./dosti.sh                    # Interactive menu
```

---

## Directory Structure

```text
07-dosti-tracker/
│
├── README.md
├── dosti.sh
├── data/
│   └── habits.txt
│
└── screenshots/
```

---

## Learning Verification

Students can inspect `dosti.sh` and locate:
* **Input handling:** CLI argument parsing (`$1`, `$2`) and interactive `read` prompts.
* **Variables:** Path configurations (`DATA_FILE`, `DIR`) and status strings.
* **Conditions:** `if [[ ... ]]`, `case` blocks for command dispatch.
* **Loops:** `while IFS=: read -r habit streak last_date; do ...` iterating over records.
* **File writing:** Atomic and appended writes (`>>`, `mv`) to `data/habits.txt`.
* **Functions:** Modular procedures (`cmd_add`, `cmd_update`, `cmd_remove`, `cmd_list`, `cmd_vstreak`).
