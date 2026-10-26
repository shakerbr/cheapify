# Deck build

Everything for the pitch deck lives inside the project. Nothing is kept outside the project directory.

## Layout

| Path | What it is | In git |
| :--- | :--- | :--- |
| `build_deck.py` | Builds `../Cheapify-GIZ-Pitch.pptx`, `../Cheapify-GIZ-Pitch.pdf` and `../presenter-guide.md` | yes |
| `deck_data.py` | All slide text: headlines, speaker notes, key numbers, calculations, Q&A, references | yes |
| `deckkit.py`, `slides_a.py`, `slides_b.py`, `assets.py` | Drawing helpers, slide builders, evidence crops/icons | yes |
| `specs/` | Deck specs v1–v4 (v4 = current, awaiting founder approval) | yes |
| `requirements.txt` | Pinned Python dependencies | yes |
| `../../tmp/venv/` | Project virtualenv | no (git-ignored) |
| `../../tmp/deck-qa/` | QA renders, static/QA-state builds, smoke tests | no (git-ignored) |

## Setup (once, from the project root)

```bash
python3 -m venv --system-site-packages tmp/venv
tmp/venv/bin/pip install -r presentation/build/requirements.txt
```

LibreOffice (`soffice`) must be installed — it converts the static build to PDF.

## Build

```bash
tmp/venv/bin/python presentation/build/build_deck.py
```

Options: `--static` (static PPTX only), `--qa-states` (also render intermediate animation states), `--qa-dir` (default `tmp/deck-qa`).

## Rules

- Never edit `presenter-guide.md` by hand — edit `deck_data.py` and rebuild.
- Do not change the deck without founder approval (`agent/rules.md` rule 14).
- Fonts: Comfortaa is embedded; Inter and IBM Plex Sans Arabic must be installed on the presenting computer.
