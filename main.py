#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters - make.fun entry.

Writes one Wi-Fi network name to /output/entry.txt. The name is fixed: it is
the entry itself, picked by a local head-to-head tournament over 18 fresh
candidate names scored against the judge's published brief (joke first, then
how much story it carries, then freshness and tight wording).

    She left. The Wi-Fi stayed.

Two beats, 27 characters: she left (the character, the event - a breakup)
and the Wi-Fi stayed (the aftermath - the network outlasted the
relationship). A stranger reading a phone's network list gets the whole
story in five words, no explanation needed.

No network, no input, no randomness: the same text on every run, so the
two grading runs agree.
"""

import os

NAME = "She left. The Wi-Fi stayed."


def main() -> None:
    # Fail loudly instead of writing a text the gate would refuse:
    # UTF-8, 1-32 characters, not only white space.
    if not 1 <= len(NAME) <= 32:
        raise ValueError("entry must be 1-32 characters")
    if not NAME.strip():
        raise ValueError("entry must not be only white space")
    NAME.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
