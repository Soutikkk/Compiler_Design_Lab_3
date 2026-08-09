# Comment Removal and Lexical Error Recovery
# For C Source Code

def process_c_file(input_file, output_file, error_file):
    NONE = 0
    SLASH = 1
    SINGLE_COMMENT = 2
    MULTI_COMMENT = 3
    STAR = 4
    STRING = 5

    state = NONE

    line = 1
    column = 1

    string_start_line = 1
    string_start_column = 1

    with open(input_file, "r") as inp, \
         open(output_file, "w") as out, \
         open(error_file, "w") as err:

        while True:
            c = inp.read(1)

            if c == "":
                break

            # ---------------- DEFAULT STATE ----------------
            if state == NONE:

                if c == "/":
                    state = SLASH

                elif c == '"':
                    out.write(c)

                    string_start_line = line
                    string_start_column = column

                    state = STRING

                elif c in "@$":
                    err.write(
                        f"[Lexical Error] Line {line}, Col {column}: "
                        f"Illegal character '{c}' encountered. Discarded.\n"
                    )

                else:
                    out.write(c)

            # ---------------- AFTER '/' ----------------
            elif state == SLASH:

                if c == "/":
                    state = SINGLE_COMMENT

                elif c == "*":
                    state = MULTI_COMMENT

                else:
                    # Previous '/' was not a comment
                    out.write("/")
                    
                    if c == '"':
                        out.write(c)

                        string_start_line = line
                        string_start_column = column

                        state = STRING
                    else:
                        out.write(c)
                        state = NONE

            # ---------------- SINGLE LINE COMMENT ----------------
            elif state == SINGLE_COMMENT:

                if c == "\n":
                    out.write("\n")
                    state = NONE

            # ---------------- MULTI LINE COMMENT ----------------
            elif state == MULTI_COMMENT:

                if c == "*":
                    state = STAR

                elif c == "\n":
                    # Preserve newline for line count/layout
                    out.write("\n")

            # ---------------- POSSIBLE END OF MULTI COMMENT ----------------
            elif state == STAR:

                if c == "/":
                    state = NONE

                elif c == "*":
                    state = STAR

                else:
                    if c == "\n":
                        out.write("\n")

                    state = MULTI_COMMENT

            # ---------------- STRING LITERAL ----------------
            elif state == STRING:

                out.write(c)

                if c == "\\":
                    # Handle escaped characters such as \" and \\
                    escaped = inp.read(1)

                    if escaped != "":
                        out.write(escaped)

                        if escaped == "\n":
                            line += 1
                            column = 0

                        column += 1

                elif c == '"':
                    state = NONE

                elif c == "\n":
                    err.write(
                        f"[Lexical Error] Line {string_start_line}, "
                        f"Col {string_start_column}: "
                        f"Unterminated string literal before newline. "
                        f"Resynchronized.\n"
                    )

                    state = NONE

            # ---------------- POSITION TRACKING ----------------
            if c == "\n":
                line += 1
                column = 1
            else:
                column += 1

        # ---------------- EOF ERROR CHECK ----------------

        if state == MULTI_COMMENT or state == STAR:
            err.write(
                f"[Lexical Error] Line {line}, Col {column}: "
                f"Unterminated block comment.\n"
            )

        if state == STRING:
            err.write(
                f"[Lexical Error] Line {string_start_line}, "
                f"Col {string_start_column}: "
                f"Unterminated string literal at EOF.\n"
            )

    print("Processing completed successfully.")
    print("Generated:")
    print("  output.c")
    print("  errors.log")


# Run the program
process_c_file(
    "input.c",
    "output.c",
    "errors.log"
)