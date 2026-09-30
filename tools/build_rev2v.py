#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

BASE = Path("NUSA_UV5RH_PRO_V2_REV2R_APRS_CTRL_FIX_BOARDV1.dat")
OUT  = Path("NUSA_UV5RH_BOARDV1_REV2V_MANUAL_BEACON_OEM_QUEUE.dat")

BASE_SHA256 = "03e8a3a47dd2f133112013261db83e4b201062cc9b519fc909427d949670276d"
OUT_SHA256  = "744352003e74f39d0dfe2d53126a7bd29be09c0c7ad130708489dd12143939b4"

PATCHES = {
    0x000115CC: bytes.fromhex("98388873"),
    0x00033FE4: bytes.fromhex("9e"),
    0x00061C50: bytes.fromhex(
        "8a3adcda598acf19d87dd1e8cd83508f"
        "c079cd83508fd875cc82ca23c8d84aa0"
        "c08ed88f9d2cc8c06194c8c090cac8e8"
    ),
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

if not BASE.is_file():
    sys.exit(f"Missing base firmware: {BASE}")

data = bytearray(BASE.read_bytes())
if len(data) != 401488:
    sys.exit(f"Unexpected base size: {len(data)}")

if sha256(data) != BASE_SHA256:
    sys.exit("REV2R base SHA-256 mismatch")

for offset, patch in PATCHES.items():
    data[offset:offset + len(patch)] = patch

result = bytes(data)
if sha256(result) != OUT_SHA256:
    sys.exit("REV2V output SHA-256 mismatch")

OUT.write_bytes(result)
print(f"Built {OUT}")
print(f"Size: {len(result)}")
print(f"SHA-256: {sha256(result)}")
