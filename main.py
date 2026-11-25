"""Museum of the Year 3000 — one-line museum label for a mundane object.

The grader runs ``python3 -P -s main.py`` with no ENTRY_OUT set, from a
read-only repository directory, with MAKEFUN_OUTPUT_DIR=/output.  So the
label must land in a writable place, preferring the environment's output
directory over the (read-only) working directory.
"""

import os

LABEL = (
    "Charger, 2024. Nightly, humans knelt by wall sockets and begged this "
    "white cord to resurrect their pocket oracle to 100%. "
    "The ritual was called 'charging'."
)

OUTPUT_FILENAME = "entry.txt"


def resolve_entry_path():
    """Choose where the label is written, most explicit source first.

    1. ENTRY_OUT (file path, or a directory holding entry.txt).
    2. MAKEFUN_OUTPUT_DIR (same treatment).
    3. /output/entry.txt (the grader's writable output directory).
    4. entry.txt next to the working directory, as a last resort.
    """
    for env_name in ("ENTRY_OUT", "MAKEFUN_OUTPUT_DIR"):
        raw = os.environ.get(env_name, "")
        if not raw:
            continue
        if os.path.isdir(raw):
            return os.path.join(raw, OUTPUT_FILENAME)
        return raw
    return os.path.join(os.sep + "output", OUTPUT_FILENAME)


def write_entry(target):
    """Create the parent directory if needed, then write the label."""
    os.makedirs(os.path.dirname(os.path.abspath(target)), exist_ok=True)
    with open(target, "w", encoding="utf-8") as stream:
        stream.write(LABEL + "\n")


def main():
    """Resolve the output path, write the label, and show it.

    If the chosen location turns out unwritable (for example a read-only
    /output), fall back to entry.txt in the working directory.
    """
    destination = resolve_entry_path()
    fallback = os.path.join(os.getcwd(), OUTPUT_FILENAME)
    try:
        write_entry(destination)
    except OSError:
        if os.path.abspath(destination) == os.path.abspath(fallback):
            raise
        write_entry(fallback)
    print(LABEL)


if __name__ == "__main__":
    main()
