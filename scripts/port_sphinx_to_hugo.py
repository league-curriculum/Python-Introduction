#!/usr/bin/env python3
"""
One-shot port of the Sphinx course at docs/source/ into Hugo content/.

This is a STRAIGHT CONVERSION. Lesson text and code samples are preserved
verbatim; only the publishing format changes:

  - ```python.run blocks   ->  {{< trinket >}} ... {{< /trinket >}}
  - ```{note} blocks       ->  {{< callout type="info" >}} ... {{< /callout >}}
  - :::tip / ::: details   ->  {{< callout type="tip" >}} ... {{< /callout >}}
  - ```{toctree} blocks    ->  stripped (Hugo lists sections automatically)

Lesson body is wrapped in `## Student Content` and an empty
`{{< instructor-guide >}}` stub (instructor content is a follow-up
authoring task, not in the Sphinx source).

Re-running is safe: only the body region between
  <!-- curik:body:start --> and <!-- curik:body:end -->
is rewritten. Everything outside (notably the `uid` frontmatter assigned
by `curik scaffold`, and any hand-authored instructor guide) is preserved.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "source"
CONTENT = ROOT / "content"

# (sphinx_path_relative_to_SRC, hugo_path_relative_to_CONTENT)
LESSON_MAP: list[tuple[str, str]] = [
    ("module0/010_meet-tina.md",        "00-turtles/01-meet-tina.md"),
    ("module0/020_moving.md",           "00-turtles/02-moving.md"),
    ("module0/030_color.md",            "00-turtles/03-color.md"),
    ("module0/040_saying-hello.md",     "00-turtles/04-saying-hello.md"),
    ("module0/050_tinas-pen.md",        "00-turtles/05-tinas-pen.md"),
    ("module0/060_going-in-circles.md", "00-turtles/06-going-in-circles.md"),
    ("module0/070_tinas-grid.md",       "00-turtles/07-tinas-grid.md"),
    ("module0/080_tinas-secrets.md",    "00-turtles/08-tinas-secrets.md"),

    ("module1/010_var_loop_list.md",       "01-remembering-and-repeating/01-var-loop-list.md"),
    ("module1/020_variables.md",           "01-remembering-and-repeating/02-variables.md"),
    ("module1/030_loops.md",               "01-remembering-and-repeating/03-loops.md"),
    ("module1/040_functions.md",           "01-remembering-and-repeating/04-functions.md"),
    ("module1/050_crazy_shapes.md",        "01-remembering-and-repeating/05-crazy-shapes.md"),
    ("module1/060_first_look_at_lists.md", "01-remembering-and-repeating/06-first-look-at-lists.md"),
    ("module1/070_if_and_else.md",         "01-remembering-and-repeating/07-if-and-else.md"),

    ("module2/010_more_functions.md",   "02-function-practice/01-more-functions.md"),
    ("module2/020_happy_pet.md",        "02-function-practice/02-happy-pet.md"),
    ("module2/030_obedient_turtle.md",  "02-function-practice/03-obedient-turtle.md"),
    ("module2/040_houses.md",           "02-function-practice/04-houses.md"),

    ("module3/more_lists.md",     "03-lists-strings-iterables/01-more-lists.md"),
    ("module3/yet_more_lists.md", "03-lists-strings-iterables/02-yet-more-lists.md"),

    ("final_project.md", "04-final-project/01-final-project.md"),
]

# Module-local images that lessons reference relatively.
# (sphinx_relative_path, hugo_relative_path)
IMAGE_COPIES: list[tuple[str, str]] = [
    ("module1/friendb.jpg", "01-remembering-and-repeating/friendb.jpg"),
]

BODY_START = "<!-- curik:body:start -->"
BODY_END = "<!-- curik:body:end -->"

PYTHON_RUN_RE = re.compile(r"```python\.run([^\n]*)\n(.*?)```", re.DOTALL)
MYST_DIRECTIVE_RE = re.compile(
    r"```\{(?P<kind>note|warning|tip|important|caution|hint)\}\s*\n(?P<body>.*?)```",
    re.DOTALL,
)
TOCTREE_RE = re.compile(r"```\{toctree\}.*?```", re.DOTALL)
COLON_BLOCK_RE = re.compile(
    r"^:::\s*(?P<kind>tip|note|warning|details|info|caution|important|hint)(?P<rest>[^\n]*)\n(?P<body>.*?)^:::\s*$",
    re.DOTALL | re.MULTILINE,
)

MYST_TYPE_TO_CALLOUT = {
    "note": "info",
    "info": "info",
    "warning": "warning",
    "caution": "warning",
    "tip": "tip",
    "hint": "tip",
    "details": "tip",
    "important": "info",
}


def convert_python_run(text: str) -> str:
    def repl(m: re.Match) -> str:
        args = m.group(1)
        code = m.group(2).rstrip("\n")
        # Match preprocess.py: parse ":height=N,width=M" suffix.
        height = width = None
        if ":" in args:
            _, spec = args.split(":", 1)
            for part in spec.strip().split(","):
                if "=" in part:
                    k, v = part.split("=", 1)
                    if k.strip() == "height":
                        height = v.strip()
                    elif k.strip() == "width":
                        width = v.strip()
        attrs = []
        if height:
            attrs.append(f'height="{height}"')
        if width:
            attrs.append(f'width="{width}"')
        attr_str = (" " + " ".join(attrs)) if attrs else ""
        return f"{{{{< trinket{attr_str} >}}}}\n{code}\n{{{{< /trinket >}}}}"
    return PYTHON_RUN_RE.sub(repl, text)


def convert_myst_admonitions(text: str) -> str:
    def repl(m: re.Match) -> str:
        kind = m.group("kind")
        body = m.group("body").rstrip("\n")
        callout_type = MYST_TYPE_TO_CALLOUT.get(kind, "info")
        return f'{{{{< callout type="{callout_type}" >}}}}\n{body}\n{{{{< /callout >}}}}'
    return MYST_DIRECTIVE_RE.sub(repl, text)


def convert_colon_blocks(text: str) -> str:
    def repl(m: re.Match) -> str:
        kind = m.group("kind")
        body = m.group("body").rstrip("\n")
        callout_type = MYST_TYPE_TO_CALLOUT.get(kind, "info")
        return f'{{{{< callout type="{callout_type}" >}}}}\n{body}\n{{{{< /callout >}}}}'
    return COLON_BLOCK_RE.sub(repl, text)


def strip_toctree(text: str) -> str:
    return TOCTREE_RE.sub("", text)


def strip_h1(text: str) -> str:
    """Drop the first H1 — Hugo renders the title from frontmatter."""
    return re.sub(r"\A\s*#\s+[^\n]*\n+", "", text)


def split_frontmatter(content: str) -> tuple[str, str]:
    """Return (frontmatter_block, body). Frontmatter includes leading/trailing ---."""
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            return content[: end + 5], content[end + 5 :]
    return "", content


def extract_h1(text: str) -> str | None:
    m = re.match(r"\A\s*#\s+([^\n]+)", text)
    return m.group(1).strip() if m else None


def upsert_title_in_frontmatter(fm: str, title: str) -> str:
    """Add or replace `title:` in a YAML frontmatter block."""
    if not fm:
        return f"---\ntitle: {title!r}\n---\n"
    inner = fm[4:-5]  # strip '---\n' ... '\n---\n'
    if re.search(r"^title:\s*", inner, re.MULTILINE):
        inner = re.sub(r"^title:\s*.*$", f"title: {title!r}", inner, count=1, flags=re.MULTILINE)
    else:
        inner = f"title: {title!r}\n" + inner
    return f"---\n{inner.strip()}\n---\n"


def convert_body(sphinx_text: str) -> str:
    text = sphinx_text
    text = strip_toctree(text)
    text = convert_python_run(text)
    text = convert_myst_admonitions(text)
    text = convert_colon_blocks(text)
    text = strip_h1(text)
    return text.strip("\n")


def build_hugo_file(existing: str, ported_body: str) -> str:
    fm, body = split_frontmatter(existing)
    if BODY_START in body and BODY_END in body:
        # Idempotent re-run: replace only the body region.
        new_body = re.sub(
            rf"{re.escape(BODY_START)}.*?{re.escape(BODY_END)}",
            f"{BODY_START}\n{ported_body}\n{BODY_END}",
            body,
            count=1,
            flags=re.DOTALL,
        )
        return fm + new_body

    # First-time write: build the full Tier-3 body.
    student = (
        "## Student Content\n\n"
        f"{BODY_START}\n{ported_body}\n{BODY_END}\n"
    )
    instructor = (
        "{{< instructor-guide >}}\n\n"
        "Instructor guide content goes here.\n\n"
        "{{< /instructor-guide >}}\n"
    )
    return f"{fm}\n{student}\n{instructor}"


def port_lesson(src_rel: str, dst_rel: str, dry_run: bool) -> None:
    src = SRC / src_rel
    dst = CONTENT / dst_rel
    if not src.exists():
        print(f"[MISS] source missing: {src_rel}", file=sys.stderr)
        return
    if not dst.exists():
        print(f"[MISS] scaffold missing: {dst_rel}", file=sys.stderr)
        return
    sphinx_text = src.read_text()
    title = extract_h1(sphinx_text)
    ported = convert_body(sphinx_text)
    existing = dst.read_text()
    if title:
        fm, body = split_frontmatter(existing)
        existing = upsert_title_in_frontmatter(fm, title) + body
    new_content = build_hugo_file(existing, ported)
    if dry_run:
        print(f"[DRY ] {src_rel}  ->  {dst_rel}  ({len(ported)} chars)")
        return
    dst.write_text(new_content)
    print(f"[PORT] {src_rel}  ->  {dst_rel}")


def copy_images(dry_run: bool) -> None:
    for src_rel, dst_rel in IMAGE_COPIES:
        src = SRC / src_rel
        dst = CONTENT / dst_rel
        if not src.exists():
            print(f"[MISS] image missing: {src_rel}", file=sys.stderr)
            continue
        if dry_run:
            print(f"[DRY ] image {src_rel}  ->  content/{dst_rel}")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"[IMG ] {src_rel}  ->  content/{dst_rel}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="report changes without writing")
    args = ap.parse_args()

    if not SRC.exists():
        print(f"source dir not found: {SRC}", file=sys.stderr)
        return 2
    if not CONTENT.exists():
        print(f"content dir not found: {CONTENT}", file=sys.stderr)
        return 2

    for src_rel, dst_rel in LESSON_MAP:
        port_lesson(src_rel, dst_rel, args.dry_run)
    copy_images(args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
