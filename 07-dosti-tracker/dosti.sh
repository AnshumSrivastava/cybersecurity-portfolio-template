#!/usr/bin/env bash
# dosti.sh — Command-line habit & accountability tracker
# Combines: variables, input, conditions, loops, functions, and file handling.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${SCRIPT_DIR}/data"
DATA_FILE="${DATA_DIR}/habits.txt"

# Ensure data storage exists
mkdir -p "$DATA_DIR"
touch "$DATA_FILE"

# Functions

cmd_list() {
    echo "=========================================="
    echo "            TRACKED HABITS                "
    echo "=========================================="
    if [[ ! -s "$DATA_FILE" ]]; then
        echo "No habits tracked yet. Use './dosti.sh add <habit>' to begin."
        return 0
    fi

    printf "%-25s | %-10s | %-12s\n" "Habit" "Streak" "Last Updated"
    echo "---------------------------------------------------------"
    while IFS=":" read -r habit streak last_date; do
        [[ -z "$habit" ]] && continue
        printf "%-25s | %-10s | %-12s\n" "$habit" "$streak days" "$last_date"
    done < "$DATA_FILE"
}

cmd_add() {
    local habit="$1"
    if [[ -z "$habit" ]]; then
        echo "Error: Habit name cannot be empty." >&2
        return 1
    fi

    # Check if habit already exists
    if grep -iq "^${habit}:" "$DATA_FILE"; then
        echo "Habit '$habit' is already being tracked."
        return 0
    fi

    echo "${habit}:0:Never" >> "$DATA_FILE"
    echo "Added habit: '$habit' (Starting streak: 0 days)"
}

cmd_update() {
    local habit="$1"
    if [[ -z "$habit" ]]; then
        echo "Error: Specify habit to update." >&2
        return 1
    fi

    if ! grep -iq "^${habit}:" "$DATA_FILE"; then
        echo "Error: Habit '$habit' not found." >&2
        return 1
    fi

    local today
    today="$(date +'%Y-%m-%d')"
    local temp_file
    temp_file="$(mktemp)"

    local updated=false
    while IFS=":" read -r h streak last_date; do
        [[ -z "$h" ]] && continue
        if [[ "${h,,}" == "${habit,,}" ]]; then
            local new_streak=$((streak + 1))
            echo "${h}:${new_streak}:${today}" >> "$temp_file"
            echo "Updated '$h'! New streak: $new_streak day(s)."
            updated=true
        else
            echo "${h}:${streak}:${last_date}" >> "$temp_file"
        fi
    done < "$DATA_FILE"

    mv "$temp_file" "$DATA_FILE"
}

cmd_remove() {
    local habit="$1"
    if [[ -z "$habit" ]]; then
        echo "Error: Specify habit to remove." >&2
        return 1
    fi

    if ! grep -iq "^${habit}:" "$DATA_FILE"; then
        echo "Error: Habit '$habit' not found." >&2
        return 1
    fi

    local temp_file
    temp_file="$(mktemp)"
    grep -iv "^${habit}:" "$DATA_FILE" > "$temp_file" || true
    mv "$temp_file" "$DATA_FILE"
    echo "Removed habit: '$habit'"
}

cmd_vstreak() {
    local habit="$1"
    if [[ -z "$habit" ]]; then
        echo "Error: Specify habit name." >&2
        return 1
    fi

    local found=false
    while IFS=":" read -r h streak last_date; do
        [[ -z "$h" ]] && continue
        if [[ "${h,,}" == "${habit,,}" ]]; then
            echo "$h"
            echo "Current streak: $streak days (Last: $last_date)"
            found=true
            break
        fi
    done < "$DATA_FILE"

    if [[ "$found" == false ]]; then
        echo "Error: Habit '$habit' not found." >&2
        return 1
    fi
}

interactive_menu() {
    echo "=========================================="
    echo "         DOSTI HABIT TRACKER              "
    echo "=========================================="
    echo "1. List habits"
    echo "2. Add a habit"
    echo "3. Update habit (mark completed)"
    echo "4. View streak"
    echo "5. Remove a habit"
    echo "6. Exit"
    echo "------------------------------------------"
    read -r -p "Choose an option [1-6]: " choice

    case "$choice" in
        1) cmd_list ;;
        2)
            read -r -p "Enter new habit name: " h_name
            cmd_add "$h_name"
            ;;
        3)
            read -r -p "Enter habit name to update: " h_name
            cmd_update "$h_name"
            ;;
        4)
            read -r -p "Enter habit name: " h_name
            cmd_vstreak "$h_name"
            ;;
        5)
            read -r -p "Enter habit name to remove: " h_name
            cmd_remove "$h_name"
            ;;
        6)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid option."
            ;;
    esac
}

# Main entrypoint
action="${1:-""}"

case "$action" in
    add)
        cmd_add "${2:-""}"
        ;;
    update)
        cmd_update "${2:-""}"
        ;;
    remove)
        cmd_remove "${2:-""}"
        ;;
    list)
        cmd_list
        ;;
    vstreak)
        cmd_vstreak "${2:-""}"
        ;;
    "")
        interactive_menu
        ;;
    *)
        echo "Usage: $0 {add <habit>|update <habit>|remove <habit>|list|vstreak <habit>}"
        exit 1
        ;;
esac
