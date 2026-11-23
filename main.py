"""Warning Label for Humans: One Line, Big Laugh.

The program writes a single-line safety warning label for every human
being to /output/entry.txt. The label imitates a real printed warning:
an all-caps WARNING opener, a plain statement of a human behaviour, and
the joke landing in the last few words, where the claim collapses.
"""

import os

LABEL_PARTS = (
    "WARNING: This human says ",
    '"I\'m five minutes away"',
    " and is still at home.",
)

MAX_CHARS = 160


def compose_label(parts: tuple[str, ...]) -> str:
    """Join the label's parts into one printed line.

    The parts mirror a real warning label's rhythm: the WARNING opener,
    the human's own quoted claim, then the twist that undercuts it in
    the last few words.
    """
    return "".join(parts).strip()


def validate(text: str) -> str:
    """Enforce the gate: 1-160 chars, single line, not blank."""
    if not text.strip():
        raise ValueError("label is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"label is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    return text


def build_label() -> str:
    """Return the one-line label, composed and validated."""
    return validate(compose_label(LABEL_PARTS))


def main() -> None:
    text = build_label()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
