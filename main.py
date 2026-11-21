"""Write the entry joke to /output/entry.txt."""

import os

JOKE = (
    "My AI agent aced the demo twice in rehearsal; "
    "live on stage, it improvised — a brand-new crash."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
