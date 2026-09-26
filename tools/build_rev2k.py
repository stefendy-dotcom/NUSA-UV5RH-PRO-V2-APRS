#!/usr/bin/env python3
from pathlib import Path
import hashlib
import urllib.request

STOCK_URL = "https://raw.githubusercontent.com/kholdfuzion/Baofeng-5RHPRO-RE/master/firmware/BF_5RH_501_v2_0_9.dat"
STOCK_SHA256 = "db97ac883de493720e8dc1677fe1e77be2aa6d981d6d30a0033a47590ef84855"
OUTPUT = Path("NUSA_UV5RH_PRO_V2_REV2K_APRS_PACKET_DETAIL.dat")
OUTPUT_SHA256 = "04bc1e1f9212f85416f9400e3791d494ed8741c9f26f188be01bb97a367851bb"

PATCHES = {
    0x000055B6: 0xD8, 0x000055B7: 0x8C, 0x000055B8: 0xDC, 0x000055B9: 0xF8,
    0x000055BA: 0x88, 0x000055BB: 0x3E, 0x000055BC: 0x37, 0x000055BD: 0xBA,
    0x000055BE: 0x99, 0x000055BF: 0xD2, 0x000055C0: 0xC9, 0x000055C1: 0xA8,
    0x000055C2: 0xB8, 0x000055C3: 0x8F,
    0x0000787E: 0x98,
    0x0000812C: 0x37, 0x0000812D: 0xE9, 0x0000812E: 0xC8, 0x0000812F: 0x77,
    0x0000814A: 0x98, 0x0000814B: 0xE8, 0x0000814C: 0xC8, 0x0000814D: 0x77,
    0x00008156: 0xD6, 0x00008157: 0xE8, 0x00008158: 0xC8, 0x00008159: 0x77,
    0x0000D5C0: 0xC9, 0x0000D5C1: 0xE8, 0x0000D5C2: 0xC8, 0x0000D5C3: 0x77,
    0x000135CA: 0xC8, 0x000135CB: 0x77,
    0x00013B91: 0x28,
    0x00016AB0: 0xC8, 0x00016AB1: 0xE8, 0x00016AB2: 0xC8, 0x00016AB3: 0x77,
    0x00016AB4: 0xC8, 0x00016AB5: 0x77, 0x00016AB6: 0xC8, 0x00016AB7: 0x77,
    0x00016AB8: 0xC8, 0x00016AB9: 0x77, 0x00016ABA: 0xC8, 0x00016ABB: 0x77,
}

def sha256(data):
    return hashlib.sha256(data).hexdigest()

with urllib.request.urlopen(STOCK_URL) as r:
    data = bytearray(r.read())

if len(data) != 401488:
    raise SystemExit(f"Unexpected stock size: {len(data)}")

stock_hash = sha256(data)
if stock_hash != STOCK_SHA256:
    raise SystemExit(f"Stock SHA256 mismatch: {stock_hash}")

for offset, value in PATCHES.items():
    data[offset] = value

out_hash = sha256(data)
if out_hash != OUTPUT_SHA256:
    raise SystemExit(f"REV2K SHA256 mismatch: {out_hash}")

OUTPUT.write_bytes(data)
print(f"Built {OUTPUT} ({len(data)} bytes)")
print(f"SHA256 {out_hash}")
