#!/usr/bin/env python3
from pathlib import Path
import hashlib

BASE = Path("NUSA_UV5RH_PRO_V2_REV2K_APRS_PACKET_DETAIL.dat")
OUTPUT = Path("NUSA_UV5RH_PRO_V2_REV2R_APRS_CTRL_FIX_BOARDV1.dat")

BASE_SHA256 = "04bc1e1f9212f85416f9400e3791d494ed8741c9f26f188be01bb97a367851bb"
OUTPUT_SHA256 = "03e8a3a47dd2f133112013261db83e4b201062cc9b519fc909427d949670276d"

# Direct patches to the encrypted .dat container, derived byte-for-byte from the
# field-tested REV2R image. Header/updater identification is intentionally retained.
PATCHES = [
    (0x00130C, bytes.fromhex("e8")),
    (0x00131E, bytes.fromhex("e8")),
    (0x001418, bytes.fromhex("c8c8c8c8")),
    (0x0079EC, bytes.fromhex("af")),
    (0x008350, bytes.fromhex("9138d674")),
    (0x00D5C0, bytes.fromhex("0b3b48d8")),
    (0x033FDE, bytes.fromhex("869d9b89e8fa9a")),
    (0x05DCD4, bytes.fromhex("98")),
    (0x05DCD6, bytes.fromhex("c2")),
    (0x05DCD8, bytes.fromhex("7a")),
    (0x05DCDA, bytes.fromhex("2a")),
    (0x05DCDC, bytes.fromhex("8d")),
    (0x05DCDE, bytes.fromhex("f9")),
    (0x05DCE0, bytes.fromhex("00")),
    (0x05DCE2, bytes.fromhex("08")),
    (0x05DCE6, bytes.fromhex("87")),
    (0x05DCE8, bytes.fromhex("dd")),
    (0x05DCEA, bytes.fromhex("7e")),
    (0x05DCEC, bytes.fromhex("10")),
    (0x05DCEE, bytes.fromhex("88")),
    (0x05DCF0, bytes.fromhex("f0")),
    (0x05DCF2, bytes.fromhex("07")),
    (0x061B90, bytes.fromhex("cfeadb30ca088438a8c4cb30ca08cffa428a3e1bcbea929c1730cce8d88fc8c8cd5bc8c0")),
]

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

data = bytearray(BASE.read_bytes())
if len(data) != 401488:
    raise SystemExit(f"Unexpected REV2K size: {len(data)}")
if sha256(data) != BASE_SHA256:
    raise SystemExit(f"REV2K SHA256 mismatch: {sha256(data)}")

for offset, patch in PATCHES:
    data[offset:offset + len(patch)] = patch

result = bytes(data)
if sha256(result) != OUTPUT_SHA256:
    raise SystemExit(f"REV2R SHA256 mismatch: {sha256(result)}")

OUTPUT.write_bytes(result)
print(f"Built {OUTPUT} ({len(result)} bytes)")
print(f"SHA256 {sha256(result)}")
