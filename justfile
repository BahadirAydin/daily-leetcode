# Shortcuts for scripts/. Run `just` with no arguments to list these.

default:
    @just --list

# Scaffold a new problem, e.g. `just new 42 --fetch`
new *ARGS:
    python3 scripts/new_problem.py {{ARGS}}

# Regenerate README stats, list progress, and the solved table
update:
    python scripts/update_readme.py

# Print a random unsolved problem number
random:
    python scripts/random_problem.py
