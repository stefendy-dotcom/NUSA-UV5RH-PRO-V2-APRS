#!/usr/bin/env python3
from pathlib import Path
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
CP_ZLIB_HEX = (
    "78daeddd3b7354751cc7e1ff66b3045744842882882b285e816473817823e1124005314c64a00187a152a161b494c696b1b4f43538be00df810e8535"
    "85858585a505633cfb23ec4f8224444940789e99c3e13327c97ed95966c366672865ae33eb4a195f5ffd664b756cab8e91ea18ab8ef1ea98fa87eb37"
    "74ae1f3a3a7d7ca2d5fe70e6f3c1d303a7876766da03edd11d03633bda63adc176f56bb95a7efb6366a6a7fb595fefeb8f63d6a50200000000000000"
    "00000000000000000000000000000000000000000000ccdc6373ffffe16f171abcc88f5ff0f667353bbfd46bcd7ae7bcb25ed6c5a79672a85cba544a"
    "abfbf57a7a5734e7fbba5f9cfbf4ec85cfceddb5fbffcf25beff6bb7f4bd7f4c749cba70fe5c6bf03e7aa0ce79bcd865975d76fddf772dfcf1579778"
    "cf99eaa9767c7d3565fc6e1c8b7efedb58afdfcbef8f4a69f4f7975a7375f3faedd57aea77e976efab871db7d168346ffa7eb2fe6bdfcab98fbf87a9"
    "4bb3563af741df4f2bbff1f85d86e7834663edf0e9799e2666cafc4f23aebbeebaebaebbeebaebaebbeebaeb7778fda1fff7575fb9f97e99d30bbfca"
    "d357eba9f736aabbb2dd5f9a7db545dfafb31f5af684e5effbe0f5d0eafc43ef950d1b9aa5b5d0b96c2d5baf55e79ecb3d97e73bdfeef67aafdcf2fa"
    "a2d65a6b7d277d5755cf47b5ef87d6346a4bf4f5177cfebdd6fd3958a371d39ff4ef3df7faf2f7529938766a7ae260f9e5e4e45875ee5bd56e96b2f3"
    "93523b7178ff8176aba7b44259f47973b57ab23a7db7e9e7f2fb97f572794529d31f6d1f993ad23a3a7d7ca2357978eac88989a903adbd275bd76ffb"
    "0ede77f5d58fe576c7bfddf9a09cfffbcfe3677f1e5df65d387ff1e3b3175b03f1eea79eec76bc452d7ba8d3bdd9c3f1b7267ba4d32bb2473bdd97bd"
    "2bdeea96bdbbd38f648f5d7f5fdc8d1e1ce8f4a3d9b16f5576ec7b2c3bf6adce8e7d8f67c7be35d9b1ef89ecd8b7363bf6adcb8e7dfddd6ec7be27b3"
    "63df53d9b16f7d76ec7b3a3bf66dc88e7d1bb363df33d9b16f5376ec7b363bf66deef650ec7b2e3bf6b5b263dff3d9b16f4b76ecdb9a1dfb5ec88e7d"
    "2f66c7be6dd9b1efa5ecd8f772b78763df2bd9b1efd5ecd8f75a76ec7b3d3bf66dcf8e7d3bb263dfceecd837901dfb06b3635fbbdb23b16f283bf60d"
    "67c7be91ecd8379a1dfb7665c7beddd9b16f2c3bf6bd911dfbdecc8e7d6f757b34f6bd9d1dfbdec98e7d7bb263df7876ec9bc88e7d7bb363dfbeecd8"
    "b73f3bf61dc88e7d93ddde15fb0e66c7be43d9b1ef7076ec7b373bf6bd971dfbdecf8e7d47b263dfd1ecd8f74176ec3bd6eddd035e0f0200e081fff9"
    "1f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    "000000000000000000000000000000000000000000000000cba056fe02c8fe92fd"
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

cp = zlib.decompress(bytes.fromhex(CP_ZLIB_HEX))
if len(cp) != 131072:
    sys.exit(f"Unexpected codeplug size: {len(cp)}")
if sha256(cp) != CP_SHA256:
    sys.exit("REV3B codeplug SHA-256 mismatch")
CP_OUT.write_bytes(cp)

print(f"Built {FW_OUT} ({len(fw)} bytes)")
print(f"Firmware SHA-256: {sha256(fw)}")
print(f"Built {CP_OUT} ({len(cp)} bytes)")
print(f"Codeplug SHA-256: {sha256(cp)}")
