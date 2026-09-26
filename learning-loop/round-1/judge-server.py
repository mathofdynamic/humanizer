#!/usr/bin/env python3
"""Serve the Round 1 judge and persist judgments.md on localhost."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import webbrowser
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


ROUND_DIR = Path(__file__).resolve().parent
JUDGMENTS_PATH = ROUND_DIR / "judgments.md"
JUDGE_URL = "/judge.html"
MAX_BODY_BYTES = 2_000_000


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_judgments() -> str:
    if not JUDGMENTS_PATH.exists():
        return "# Round 1 human judgments\n"
    return JUDGMENTS_PATH.read_text(encoding="utf-8")


def write_judgments(markdown: str) -> None:
    temporary_path: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            prefix=".judgments-",
            suffix=".tmp",
            dir=ROUND_DIR,
            delete=False,
        ) as temporary_file:
            temporary_file.write(markdown)
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
            temporary_path = temporary_file.name
        os.replace(temporary_path, JUDGMENTS_PATH)
    finally:
        if temporary_path and os.path.exists(temporary_path):
            os.unlink(temporary_path)


class JudgeRequestHandler(SimpleHTTPRequestHandler):
    server_version = "HumanizerJudge/1.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROUND_DIR), **kwargs)

    def _send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _request_path(self) -> str:
        return urlsplit(self.path).path

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        path = self._request_path()
        if path == "/api/health":
            self._send_json({"ok": True, "service": "humanizer-round-1-judge"})
            return
        if path == "/api/judgments":
            self._send_json({"markdown": read_judgments(), "savedAt": utc_now()})
            return
        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        if self._request_path() != "/api/judgments":
            self.send_error(404, "Not found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            content_length = 0

        if content_length <= 0 or content_length > MAX_BODY_BYTES:
            self._send_json({"ok": False, "error": "Invalid request size."}, status=413)
            return

        try:
            payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
            markdown = payload.get("markdown") if isinstance(payload, dict) else None
            if not isinstance(markdown, str) or not markdown.lstrip().startswith("# Round 1 human judgments"):
                raise ValueError("The request must contain a Round 1 judgments Markdown document.")
            if len(markdown.encode("utf-8")) > MAX_BODY_BYTES:
                raise ValueError("The judgments document is too large.")
            write_judgments(markdown)
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError, OSError) as error:
            self._send_json({"ok": False, "error": str(error)}, status=400)
            return

        self._send_json({"ok": True, "savedAt": utc_now()})

    def log_message(self, format: str, *args) -> None:
        print(f"[judge-server] {self.address_string()} - {format % args}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Bind address; keep localhost for local-only use.")
    parser.add_argument("--port", type=int, default=8765, help="TCP port (default: 8765).")
    parser.add_argument("--no-open", action="store_true", help="Do not open the judge in the default browser.")
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), JudgeRequestHandler)
    url = f"http://{args.host}:{args.port}{JUDGE_URL}"
    print(f"Humanizer Round 1 judge running at {url}")
    print(f"Live source: {ROUND_DIR / 'candidates.md'}")
    print(f"Live judgments: {JUDGMENTS_PATH}")
    print("Press Ctrl+C to stop.")
    if not args.no_open:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping judge server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
