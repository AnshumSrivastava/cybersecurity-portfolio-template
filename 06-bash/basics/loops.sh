#!/usr/bin/env bash
# loops.sh — Demonstrating for and while loops

echo "=== For Loop: Port List Scanning ==="
for port in 21 22 80 443 8080; do
    echo "Inspecting rule for port: $port"
done

echo
echo "=== While Loop: Reading text lines ==="
counter=1
while [[ $counter -le 3 ]]; do
    echo "Processing iteration #$counter"
    ((counter++))
done
