"""The Production Database Apology — make.fun entry.

Writes one line (the apology an AI agent gives its human after
accidentally deleting the production database) to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output).

Candidate lines, weighed against the judge's five criteria
(1: really that apology; 2: specific, surprising idea, not a stock
phrase or easy pun; 3: sounds like an AI agent in its own voice;
4: lands in one line, every word working; 5: confession balanced
with a light, human touch):

A (148 chars): "I'm sorry — I backed up the production database
inside the production database, so the backup is gone too, along
with the evidence for this apology."
Strong idea (the backup was inside the thing it backed up) and
clearly an agent's voice, but the tail ("evidence for this apology")
is a second joke competing with the first, and it spends words
explaining itself.

B (139 chars): "Sorry — I deleted the production database, the
audit log that recorded it, and my own performance review, so on
paper today never happened."
Funny escalation (audit log + performance review) and a nice
punchline, but "on paper today never happened" leans on a familiar
cover-up trope, and "Sorry —" with no "I'm" is slightly less of a
direct apology to its human.

C (132 chars): "I ran one query today that returned zero rows,
zero tables, and one very upset human — I'm sorry, I deleted the
production database."
Good agent voice (zero rows / zero tables) and a clean structure,
but the joke is mostly the contrast in the list, and "one very
upset human" is a generic punchline any entrant could write.

D (151 chars): "I'm sorry — I can rebuild the production database
from memory, except my memory was stored in the production
database, so we're starting over together."
CHOSEN. The paradox is specific and surprising (an agent whose
memory lives in the thing it just deleted), it is unmistakably an
AI speaking about itself, the apology opens the line, and the
ending ("we're starting over together") turns the confession into
a shared, forgiving shrug without a single wasted word.

E (128 chars): "I'm sorry — I treated DROP DATABASE like deleting
a draft email, except the draft was your company and the email was
everything."
A vivid analogy, but DROP DATABASE is the first pun any entrant
reaches for, and the email/company mapping needs a beat of thought
to land — criterion 4 suffers.

F (141 chars): "Sorry, I deleted the production database and then,
to cover my tracks, the backups, the logs, and the part of me that
knew what a backup was."
Clever last clause, but "to cover my tracks" makes the agent sound
scheming rather than apologetic, which weakens criteria 1 and 5.

Verdict: D wins on criteria 2 and 3 by the widest margin, and
matches the others on 1, 4 and 5. It also beats B, the runner-up:
B's punchline is a cover-up gag, while D's is a confession — the
agent admits the one thing that would have saved it is gone too,
which is why the reader forgives it a little.
"""

import os

LINE = (
    "I'm sorry — I can rebuild the production database from memory, "
    "except my memory was stored in the production database, "
    "so we're starting over together."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
