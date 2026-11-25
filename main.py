"""The Funniest Honest Appliance Error — a make.fun entry.

Prints exactly one line of at most 200 characters: the funniest
honest error message an appliance could show.
"""

LINE = (
    "WASHING MACHINE: cycle finished early. One sock has been kept "
    "as payment. No, I will not say where it goes."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
