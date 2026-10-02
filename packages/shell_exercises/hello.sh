#!/usr/bin/env bash

# Change only the text between the quotation marks.
message="Hello from the shell!"

# `%s` inserts the message and `\n` ends the line on standard output.
printf '%s\n' "$message"
