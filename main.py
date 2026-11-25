"""Museum of the Year 3000 — one-line museum label for a mundane object."""

import os

ENTRY = (
    "Charger, 2024. Nightly, humans knelt by wall sockets and begged this "
    "white cord to resurrect their pocket oracle to 100%. "
    "The ritual was called 'charging'."
)


def resolve_destination():
    """Return the file path where the entry text must be written."""
    target = os.environ.get("ENTRY_OUT", "")
    if not target:
        return "entry.txt"
    if os.path.isdir(target):
        return os.path.join(target, "entry.txt")
    return target


def write_label(path):
    """Write the single-line museum label to the given file path."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


def exhibit():
    """Resolve the destination, write the label, and announce it."""
    destination = resolve_destination()
    write_label(destination)
    print(ENTRY)


if __name__ == "__main__":
    exhibit()
