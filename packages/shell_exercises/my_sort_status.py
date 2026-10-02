"""Sort standard input and report status through standard error."""
import sys

def main() -> None:
    """Write sorted lines to standard output and status to standard error."""
    # Send the sorted data to standard output so redirection can save it cleanly.
    # Send the progress message to `sys.stderr`, for example with `print(..., file=sys.stderr)`.
    lines = sys.stdin.readlines()
    try:
        sys.stdout.writelines(sorted(lines, reverse=False))
    except:
        sys.stderr.writelines("An error has occurred")


if __name__ == "__main__":
    main()
