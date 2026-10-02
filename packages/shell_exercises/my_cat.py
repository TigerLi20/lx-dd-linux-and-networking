"""Copy standard input to standard output."""
import sys

def main() -> None:

    """Read all input and write it unchanged to standard output."""
    # Read `sys.stdin` one line at a time; each line already includes its newline.
    # Write each line to `sys.stdout` unchanged so a pipeline preserves its data.
    lines = sys.stdin.readlines()
    sys.stdout.writelines(lines)
    


if __name__ == "__main__":
    main()
