#!/usr/bin/env python3
"""Generate images via Google's nano-banana (gemini-2.5-flash-image)."""
import base64
import json
import os
import sys
import urllib.request

API_KEY = os.getenv("GEMINI_API_KEY") or ""
if not API_KEY:
    raise SystemExit("Set GEMINI_API_KEY env var before running this script.")

ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent"


def generate(prompt: str, out_path: str, aspect: str = "16:9") -> None:
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect},
        },
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": API_KEY,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())

    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(base64.b64decode(inline["data"]))
                print(f"OK  {out_path}  ({os.path.getsize(out_path)//1024} KB)")
                return
    raise RuntimeError(f"No image in response: {json.dumps(data)[:500]}")


if __name__ == "__main__":
    # CLI: gen_image.py <out> <aspect> <prompt...>
    out = sys.argv[1]
    aspect = sys.argv[2]
    prompt = " ".join(sys.argv[3:])
    generate(prompt, out, aspect)
