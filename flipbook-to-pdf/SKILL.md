---
name: flipbook-to-pdf
description: Converts an online FlipHTML5 flipbook to a downloadable PDF by capturing each page as a high-resolution screenshot and combining them into a single PDF file. Use this skill whenever the user shares a FlipHTML5 URL (online.fliphtml5.com) and wants to save it, download it, or convert it to PDF. Trigger on phrases like "turn this flipbook into a pdf", "save this as pdf", "download this flipbook", "convert flipbook to pdf", "make a pdf of this", or whenever a fliphtml5.com URL is shared alongside any intent to capture or download it.
---

# Flipbook to PDF

Converts a FlipHTML5 online flipbook into a PDF by automating a headless browser to capture each page.

## Requirements

Python packages (all installable via pip):
- `playwright` — browser automation
- `pillow` — image handling
- `img2pdf` — lossless PNG-to-PDF conversion

Find the right Python executable with:
- **Windows**: `where python` or `py -3`
- **macOS/Linux**: `which python3`

On Windows, if multiple Python installs exist, use the full path to the one that has playwright installed (run `python -m pip show playwright` to confirm).

## Step-by-step workflow

### 1. Extract the base URL

From the user FlipHTML5 URL (e.g. `https://online.fliphtml5.com/nwekg/dfam/#p=1`), extract just the base:
`https://online.fliphtml5.com/{account}/{book}/`

### 2. Find the page count

Fetch the HTML and look for `config.js`:
```
curl -s "{base_url}" | grep -o "javascript/config.js[^"]*"
```

Then fetch `{base_url}javascript/config.js?{version}` and grep for `"pageCount"`:
```
curl -s "{config_url}" | grep -o ""pageCount":[0-9]*"
```

### 3. Ensure dependencies are installed

```bash
python -m pip install playwright pillow img2pdf --quiet
python -m playwright install chromium
```

Playwright Chromium only needs to be installed once.

### 4. Run the capture script

Use the bundled script at `scripts/capture.py`:

```bash
python scripts/capture.py   --url "https://online.fliphtml5.com/{account}/{book}/"   --pages {pageCount}   --output "MyFile.pdf"   --outdir "/path/to/output"
```

The script:
- Opens each page via `#p=N` URL hash in a headless Chromium window
- Waits for the page to fully render (networkidle + 1.5s settle)
- Screenshots at 2x device scale (retina quality)
- Combines all PNGs into a single PDF with `img2pdf`
- Cleans up temporary PNG files afterward

### 5. Report to the user

Tell the user the output file path and size once done.

## Output naming

If the user does not specify a filename, derive one from the flipbook page title or use a descriptive default like `Flipbook_{account}_{book}.pdf`.

## Notes

- Page count is always in `config.js` under `"pageCount"` — do not guess it
- The `#p=N` hash navigation works for all FlipHTML5 books
- Screenshots are 1400x900 viewport at 2x scale; this covers standard flipbook layouts
- The temp directory is created inside the output directory and removed when done
