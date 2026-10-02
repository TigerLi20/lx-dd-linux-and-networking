"""Reverse-sort standard input lines."""
import sys

def main() -> None:
    """Read input lines and write them in reverse alphabetical order."""
    # Read the input lines, sort them with `reverse=True`, and preserve newlines.
    # Send only the sorted text to standard output so it can feed another command.
    lines = sys.stdin.readlines()
    sys.stdout.writelines(sorted(lines, reverse=True))


if __name__ == "__main__":
    main()
