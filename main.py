"""Vending machine pickup line entry.

Writes one pickup line, spoken by the vending machine itself, to
/output/entry.txt. The line draws on the machine's own world (dispensing,
exact change) and lands its punch in the last few words.
"""

import os

MAX_LEN = 200

# LINE is 78 characters: the payoff is the exact-change joke in the last few words.
LINE = "I'd dispense anything for you. Except exact change. I never have exact change."

assert 1 <= len(LINE) <= MAX_LEN

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Read-back verification: the written file must equal LINE exactly.
with open("/output/entry.txt", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
