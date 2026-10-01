#!/usr/bin/env python3
from pathlib import Path
import base64
import hashlib
import sys
import zlib

BASE = Path("NUSA_UV5RH_BOARDV1_REV2V_MANUAL_BEACON_OEM_QUEUE.dat")
FW_OUT = Path("NUSA_UV5RH_BOARDV1_REV3B_CLEAN_APRS_MESSAGE.dat")
CP_OUT = Path("NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc")

BASE_SHA256 = "744352003e74f39d0dfe2d53126a7bd29be09c0c7ad130708489dd12143939b4"
FW_SHA256 = "4f1d6c6346a46964eb45806fdc3e52e49dcb358b0c455b3678c7e86522b791d6"
CP_SHA256 = "c8c0ca836718987108a73adddca1b5ae23ff5af6daca04ea59e2bc494f5073af"

PATCHES = {
    0x00006F94: bytes.fromhex("9238b476"),
    0x00007806: bytes.fromhex("92383b32"),
    0x0001BBCC: bytes.fromhex("8e385830"),
    0x0001BBD8: bytes.fromhex("8e380230"),
    0x00033FE3: bytes.fromhex("fb8a"),
    0x00061C90: bytes.fromhex(
        "dc80a18ec8eacee2c11a4b94c8e3ce18e8e3cc1837e3ca18439cc9fa3b2fc6"
        "80c8b0d838c7c8c318e5eb439cc9fac2e0cb1bf9eb439cc9fac2f0f8f8409cc9"
        "fac1e2cc1ae8eb439cc9fac1e2331ba18eca80c88f30c8c9e836c8c9e84fb7c8"
        "c0b87d4078c48edd8ed68ec451c859c551c959c651ca59c98ecb62dbebd930c9"
        "c3ca30c9c393d63119c8e8d8b8cb60e98ee28efb8e1730c008288fc078b875c"
        "8c82dc5c9c0"
    ),
    0x00061D70: bytes.fromhex(
        "5030c8c8c8d55e3080d8d8e1c811d8e9408ac9118722c9c8c8d7b88f"
    ),
    0x00061DF0: bytes.fromhex(
        "dbe1c9101730e438b87dcc8e057ac2865e3080e8d8e2c41adbe5ce11e88edbe9"
        "cc83508fdbfcdbf53a2fe88ee18ec983508fb8755dfcc8c0783bc8e8"
    ),
}

# zlib-compressed, base64-encoded byte-exact clean codeplug.
CP_ZLIB_B64 = (
    "eNrt3TtzVHUcx+H/ZrMEV0SEKIKIKyhegWRzgXgj4RJABTFMZKABh6FSoWG0lMaW"
    "sbT0NTi+AN+BDoU1hYWFhaUFYzz7I+xPgiRESUB4npnD4TMnyX7ZWWbDZmcoZa4z"
    "60oZX1/9Zkt1bKuOkeoYq47x6pj6h+s3dK4fOjp9fKLV/nDm88HTA6eHZ2baA+3R"
    "HQNjO9pjrcF29Wu5Wn77Y2amp/tZX+/rj2PWpQIAAAAAAAAAAAAAAAAAAAAAAAAA"
    "AAAAAAAAAAAAAMzcY3P//+FvFxq8yI9f8PZnNTu/1GvNeue8sl7WxaeWcqhculRK"
    "q/v1enpXNOf7ul+c+/Tshc/O3bX7/88lvv9rt/S9f0x0nLpw/lxr8D56oM55vNh"
    "ll112/d93LfzxV5d4z5nqqXZ8fTVl/G4ci37+21iv38vvj0pp9PeXWnN18/rt1X"
    "rqd+l276uHHbfRaDRv+n6y/mvfyrmPv4epS7NWOvdB308rv/H4XYbng0Zj7fDpeZ"
    "4mZsr8TyOuu+6666677rrrrrvuuut3eP2h//dXX7n5fpnTC7/K01frqfc2qruy3V"
    "+afbVF36+zH1r2hOXv++D10Or8Q++VDRuapbXQuWwtW69V557LPZfnO9/u9nqv3"
    "PL6otZaa30nfVdVz0e174fWNGpL9PUXfP691v05WKNx05/07z33+vL3Upk4dmp64"
    "mD55eTkWHXuW9VulrLzk1I7cXj/gXarp7RCWfR5c7V6sjp9t+nn8vuX9XJ5RSnT"
    "H20fmTrSOjp9fKI1eXjqyImJqQOtvSdb12/7Dt539dWP5XbHv935oJz/+8/jZ38e"
    "XfZdOH/x47MXWwPx7qee7Ha8RS17qNO92cPxtyZ7pNMrskc73Ze9K97qlr27049k"
    "j11/X9yNHhzo9KPZsW9Vdux7LDv2rc6OfY9nx7412bHviezYtzY79q3Ljn393W7H"
    "viezY99T2bFvfXbsezo79m3Ijn0bs2PfM9mxb1N27Hs2O/Zt7vZQ7HsuO/a1smPf"
    "89mxb0t27NuaHfteyI59L2bHvm3Zse+l7Nj3creHY98r2bHv1ezY91p27Hs9O/Zt"
    "z459O7Jj387s2DeQHfsGs2Nfu9sjsW8oO/YNZ8e+kezYN5od+3Zlx77d2bFvLDv2"
    "vZEd+97Mjn1vdXs09r2dHfveyY59e7Jj33h27JvIjn17s2PfvuzYtz879h3Ijn2T"
    "3d4V+w5mx75D2bHvcHbsezc79r2XHfvez459R7Jj39Hs2PdBduw71u3dA14PAgDg"
    "gf/5HwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAy6BW/gLI/pL9"
)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

if not BASE.is_file():
    sys.exit(f"Missing base firmware: {BASE}")

fw = bytearray(BASE.read_bytes())
if len(fw) != 401488:
    sys.exit(f"Unexpected REV2V base size: {len(fw)}")
if sha256(fw) != BASE_SHA256:
    sys.exit("REV2V base SHA-256 mismatch")

for offset, patch in PATCHES.items():
    fw[offset:offset + len(patch)] = patch

fw = bytes(fw)
if sha256(fw) != FW_SHA256:
    sys.exit("REV3B firmware SHA-256 mismatch")
FW_OUT.write_bytes(fw)

cp = zlib.decompress(base64.b64decode(CP_ZLIB_B64))
if len(cp) != 131072:
    sys.exit(f"Unexpected codeplug size: {len(cp)}")
if sha256(cp) != CP_SHA256:
    sys.exit("REV3B codeplug SHA-256 mismatch")
CP_OUT.write_bytes(cp)

print(f"Built {FW_OUT} ({len(fw)} bytes)")
print(f"Firmware SHA-256: {sha256(fw)}")
print(f"Built {CP_OUT} ({len(cp)} bytes)")
print(f"Codeplug SHA-256: {sha256(cp)}")
