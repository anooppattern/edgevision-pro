#!/usr/bin/env python3
"""Remove empty directory entries from a .pptx (OPC packages must contain only
file parts). pptxgenjs writes folder entries like ppt/charts/ and ppt/media/
that can make stricter PowerPoint builds show a "repair" prompt. Run this on
each generated deck as the final packaging step.

Usage: python3 strip_pptx_dirs.py <file.pptx> [<file2.pptx> ...]
"""
import sys, os, zipfile

def strip(path):
    tmp = path + ".clean"
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        dropped = 0
        for item in zin.infolist():
            if item.filename.endswith("/"):
                dropped += 1
                continue
            zout.writestr(item, zin.read(item.filename))
    os.replace(tmp, path)
    print("stripped {} dir-entries from {}".format(dropped, os.path.basename(path)))

if __name__ == "__main__":
    for p in sys.argv[1:]:
        strip(p)
