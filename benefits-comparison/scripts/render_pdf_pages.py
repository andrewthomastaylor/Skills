#!/usr/bin/env python3
"""Render all pages of a PDF to PNG files for visual analysis.

Use this when a PDF is image-based (scanned) and the Read tool returns no text.
Renders at 2x resolution by default; use --scale 4 for hard-to-read rate tables.

Usage:
    python3 render_pdf_pages.py "path/to/booklet.pdf" "output/pages_dir"
    python3 render_pdf_pages.py "path/to/booklet.pdf" "output/hires_dir" --scale 4
    python3 render_pdf_pages.py "path/to/booklet.pdf" "output/dir" --pages 5,6,7

Requires:
    python3 -m pip install pymupdf
"""
import sys
import os
import argparse


def render_pdf(pdf_path: str, output_dir: str, scale: int = 2, pages: list = None) -> list:
    """Render PDF pages to PNG files.

    Args:
        pdf_path: Path to the PDF file.
        output_dir: Directory to write PNG files into.
        scale: Resolution multiplier (2 = 2x screen resolution, ~144 dpi).
        pages: Optional list of 1-based page numbers to render. If None, renders all pages.

    Returns:
        List of output PNG file paths.
    """
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("PyMuPDF is not installed.")
        print("Run: python3 -m pip install pymupdf")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    mat = fitz.Matrix(scale, scale)
    output_paths = []

    total = len(doc)
    page_range = range(total)
    if pages:
        page_range = [p - 1 for p in pages if 1 <= p <= total]

    for i in page_range:
        page = doc[i]
        out_path = os.path.join(output_dir, f"page_{i + 1:02d}.png")
        pix = page.get_pixmap(matrix=mat)
        pix.save(out_path)
        output_paths.append(out_path)
        print(f"  [{i + 1}/{total}] {out_path}  ({pix.width}x{pix.height}px)")

    doc.close()
    print(f"\nDone — {len(output_paths)} page(s) written to: {output_dir}")
    return output_paths


def parse_pages(pages_str: str) -> list:
    """Parse a comma-separated list of page numbers, e.g. '5,6,7' -> [5, 6, 7]."""
    result = []
    for part in pages_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            result.extend(range(int(start), int(end) + 1))
        else:
            result.append(int(part))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Render PDF pages to PNG files for visual analysis."
    )
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("output_dir", help="Output directory for PNG files")
    parser.add_argument(
        "--scale",
        type=int,
        default=2,
        help="Resolution scale factor (default: 2; use 4 for dense rate tables)",
    )
    parser.add_argument(
        "--pages",
        type=str,
        default=None,
        help="Comma-separated page numbers to render, e.g. '5,6,7' or '5-7' (default: all pages)",
    )
    args = parser.parse_args()

    pages = parse_pages(args.pages) if args.pages else None
    render_pdf(args.pdf_path, args.output_dir, args.scale, pages)
