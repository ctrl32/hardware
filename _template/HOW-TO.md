# The board guide template

This folder is the shape of one board's guide. It is never published (the
web reads `boards/` only). A new tested board gets a copy of it under
`boards/<maker>/<slug>/`:

| File | Page |
|---|---|
| `README.md` | the overview: photo, badges, pin map, the capability table (generated - `tools/capabilities.py`), the steps |
| `hardware.md` | what you need, power, the pin map, safety |
| `install.md` | the runtime on the board, step by step, one screenshot per step |
| `configure.md` | network, I/O, communication, the display |
| `examples/README.md` | the gallery of the board's projects |
| `examples/all-in-one/` | REQUIRED: one project that uses every capability of the table |
| `examples/<task>/` | more projects, each in its own folder with README.md, the .prj32 and img/ |
| `troubleshooting.md` | Symptom / Cause / Fix |
| `img/board-NN.jpg` | the board's photos (at least 3: top, bottom, in use) |
| `pinout/pinout.svg` + `.png` | the pin map in the ctrl32 style |
| `schematics/`, `datasheets/`, `3d/` | the maker's files - only with permission, listed in NOTICE.md |
| `board.yaml` | the ctrl32 facts the capability table reads |

Rules: English first (translations beside, `README.sk.md` ...), every image
has alt text, a part that does not apply stays with one sentence saying so,
`tools/check.py` must pass.
