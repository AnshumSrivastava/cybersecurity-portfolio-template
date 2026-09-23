#!/usr/bin/env bash
# functions.sh — Modular routines, scopes, and return statuses

log_message() {
    local level="$1"
    local msg="$2"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [$level] $msg"
}

check_service() {
    local host="$1"
    local port="$2"

    log_message "INFO" "Checking reachability for $host:$port..."
    if nc -z -w 2 "$host" "$port" 2>/dev/null; then
        log_message "SUCCESS" "Connection to $host:$port established."
        return 0
    else
        log_message "WARNING" "Unable to reach $host:$port."
        return 1
    fi
}

log_message "INFO" "Starting network health verification script..."
check_service "127.0.0.1" 22 || true
log_message "INFO" "Verification complete."
