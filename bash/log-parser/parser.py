import os
import sys
import re
import json


def extract_regex(pattern_file_path):
    """
    Extracts the regular expression pattern from the markdown pattern file.
    Looks for a fenced code block with language 'regex':
    ```regex
    <pattern>
    ```
    """
    with open(pattern_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"```regex\s*\n(.*?)\n```", content, re.DOTALL)
    if not match:
        raise ValueError(f"No ```regex ... ``` code block found in {pattern_file_path}")

    return match.group(1).strip()


def parse_logs(log_file_path, pattern_file_path):
    # 1. Extract and compile regex pattern
    regex_str = extract_regex(pattern_file_path)
    pattern = re.compile(regex_str)

    total_lines = 0
    parsed_lines = 0
    malformed_lines = 0
    records = []

    # 2. Read log file line by line and apply regex
    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.rstrip("\r\n")
            if not line_str:
                continue

            total_lines += 1
            match = pattern.match(line_str)
            if match:
                parsed_lines += 1
                records.append(match.groupdict())
            else:
                malformed_lines += 1

    # 3. Build structured output
    output_data = {
        "source": log_file_path,
        "pattern": pattern_file_path,
        "summary": {
            "total_lines": total_lines,
            "parsed_lines": parsed_lines,
            "malformed_lines": malformed_lines,
        },
        "records": records,
    }

    # 4. Write JSON output
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "parsed.json")

    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(output_data, out, indent=2)

    # 5. Print summary to console
    print("Log Parser")
    print("----------")
    print()
    print("Input:")
    print(f"  {log_file_path}")
    print()
    print("Pattern:")
    print(f"  {pattern_file_path}")
    print()
    print(f"Total lines:      {total_lines}")
    print(f"Parsed lines:     {parsed_lines}")
    print(f"Malformed lines:  {malformed_lines}")
    print()
    print("Output:")
    print(f"  {output_path}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 parser.py <log_file> <pattern_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    pattern_file = sys.argv[2]

    if not os.path.exists(log_file):
        print(f"Error: Log file '{log_file}' not found.")
        sys.exit(1)

    if not os.path.exists(pattern_file):
        print(f"Error: Pattern file '{pattern_file}' not found.")
        sys.exit(1)

    parse_logs(log_file, pattern_file)


if __name__ == "__main__":
    main()
