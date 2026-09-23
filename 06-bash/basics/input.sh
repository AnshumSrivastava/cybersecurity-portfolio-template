#!/usr/bin/env bash
# input.sh — Interactive user input and validation

read -r -p "Enter target IP or hostname: " TARGET_HOST

if [[ -z "$TARGET_HOST" ]]; then
    echo "Error: No target provided." >&2
    exit 1
fi

echo "Selected target: $TARGET_HOST"
