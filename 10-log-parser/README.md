# Generic Log Parser

Raw Logs + Parsing Pattern → Structured Data

```text
Logs/
   │
   ├── apache.log
   └── login.log
        │
        │
        ▼
Patterns/
   │
   ├── apache.md
   └── login.md
        │
        │
        ▼
    parser.py
        │
        ▼
output/parsed.json
```

> `parser.py` is a generic parsing engine. The log format is defined outside the program in the `Patterns/` directory.

---

## Architecture & Concept

The central concept of this project decouples log structure rules from code logic:

```text
RAW LOG
   ↓
PATTERN
   ↓
REGEX MATCH
   ↓
NAMED CAPTURE GROUPS
   ↓
DICTIONARY
   ↓
JSON
```

### Example

**Raw Log Line:**

```text
10:42:17 LOGIN rahul FAILED
```

**Pattern Definition (`Patterns/login.md`):**

```regex
^(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<action>[A-Z]+)\s+(?P<user>[a-zA-Z]+)\s+(?P<result>SUCCESS|FAILED)$
```

**Structured JSON Output:**

```json
{
  "time": "10:42:17",
  "action": "LOGIN",
  "user": "rahul",
  "result": "FAILED"
}
```

---

## Project Structure

```text
log-parser/
│
├── Logs/
│   ├── apache.log
│   └── login.log
│
├── Patterns/
│   ├── apache.md
│   └── login.md
│
├── output/
│   └── parsed.json
│
├── parser.py
│
└── README.md
```

---

## Usage

Run the generic parser with Python's standard library:

### 1. Parse Login Logs

```bash
python3 parser.py Logs/login.log Patterns/login.md
```

### 2. Parse Apache Logs

```bash
python3 parser.py Logs/apache.log Patterns/apache.md
```

Changing the log format does not require changing the parser. Only the pattern definition changes.
