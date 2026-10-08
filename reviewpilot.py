"""ReviewPilot - Claude-powered code review & docs agent (beta).

Usage:
    python reviewpilot.py review            # reviews `git diff` (staged + unstaged)
    python reviewpilot.py docs path/to/file.py   # generates docstrings/README section
Requires: pip install anthropic ; env ANTHROPIC_API_KEY
"""
import subprocess
import sys

import anthropic

MODEL = "claude-sonnet-4-5"  # change to the model available on your Console account
client = anthropic.Anthropic()

REVIEW_PROMPT = """You are a senior engineer doing code review.
Review the following git diff. Output markdown with sections:
## Summary, ## Bugs & Risks, ## Security, ## Suggestions.
Reference file names and be concrete. Skip nitpicks.

DIFF:
{diff}"""

DOCS_PROMPT = """Write clear documentation for this source file: a short README section
plus improved docstrings for each public function/class (show them as a list).

FILE ({name}):
{code}"""


def ask(prompt: str) -> str:
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "review":
        diff = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True).stdout
        if not diff.strip():
            print("No changes to review.")
            return
        print(ask(REVIEW_PROMPT.format(diff=diff[:60000])))
    elif cmd == "docs" and len(sys.argv) > 2:
        with open(sys.argv[2], encoding="utf-8") as f:
            print(ask(DOCS_PROMPT.format(name=sys.argv[2], code=f.read()[:60000])))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
