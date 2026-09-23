#!/usr/bin/env bash
# variables.sh — Demonstrating variable handling and parameter expansion

set -euo pipefail

# User-defined variables
COURSE_NAME="Cybersecurity Fundamentals"
STUDENT_ROLE="Security Analyst"
HOST_TARGET="${1:-"127.0.0.1"}"

echo "Course: $COURSE_NAME"
echo "Role:   $STUDENT_ROLE"
echo "Target: $HOST_TARGET"

# Special parameters
echo "Script name: $0"
echo "Total arguments passed: $#"
echo "Process ID: $$"
