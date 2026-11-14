"""Spicy miso ramen photo handler.

Hands entry.png — spicy miso ramen with chilli oil swirling through
the broth, corn, butter, nori and spring onions over wavy noodles —
byte-for-byte to the output directory. The photo is copied verbatim.
"""

import os
import shutil

MISO_PHOTO = "entry.png"
MISO_ENV = "MAKEFUN_OUTPUT_DIR"
MISO_OUT_DIR = "/output"


def miso_destination_path():
    out = os.environ.get(MISO_ENV) or MISO_OUT_DIR
    return os.path.join(out, MISO_PHOTO)


def miso_source_path():
    folder = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(folder, MISO_PHOTO)


def serve_miso_ramen():
    src = miso_source_path()
    if not os.path.isfile(src):
        raise SystemExit(f"miso ramen photo not found: {src}")
    if os.path.getsize(src) < 1:
        raise SystemExit(f"miso ramen photo is empty: {src}")
    dst = miso_destination_path()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    final_size = os.path.getsize(dst)
    print(f"miso ramen photo served to {dst} ({final_size} bytes)")


if __name__ == "__main__":
    serve_miso_ramen()
