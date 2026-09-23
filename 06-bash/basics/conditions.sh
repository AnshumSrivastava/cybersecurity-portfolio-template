#!/usr/bin/env bash
# conditions.sh — Demonstrating branching logic and conditionals

PORT="${1:-80}"

if [[ "$PORT" -eq 80 ]]; then
    echo "Port $PORT corresponds to insecure HTTP."
elif [[ "$PORT" -eq 443 ]]; then
    echo "Port $PORT corresponds to secure HTTPS."
elif [[ "$PORT" -eq 22 ]]; then
    echo "Port $PORT corresponds to SSH administration."
else
    echo "Port $PORT is a custom or unclassified port."
fi

case "$PORT" in
    20|21) echo "Protocol: FTP" ;;
    25)    echo "Protocol: SMTP" ;;
    53)    echo "Protocol: DNS" ;;
    *)     echo "Protocol check completed." ;;
esac
