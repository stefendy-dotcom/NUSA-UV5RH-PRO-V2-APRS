# REV3B CLEAN Codeplug Guide

Use **NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc** as the first-test baseline for REV3B on UV-5RM / UV-5RH **hardware Board V1**.

## Why the supplied codeplug matters

During field testing, firmware behavior changed dramatically depending on APRS configuration stored in the codeplug. A problematic codeplug contained inconsistent APRS path data and other settings; with a clean codeplug the same firmware received APRS packets repeatedly without rebooting and APRS Message display became reliable.

For this reason, a firmware report is meaningful only after first testing with the supplied clean codeplug.

## Clean APRS baseline

- APRS Ctrl: ON
- VFO A: Wide
- VFO B: Wide
- APRS bandwidth: 25K
- RX packet types: PassAll, Position, Mic-E, Message
- APRS path count: 1
- APRS path: WIDE2-2
- Unused path slots: properly space-padded
- Regular/periodic APRS send: OFF
- RX callsign filter entries: cleared

Set your own APRS source callsign/SSID after loading the clean codeplug.

Do not copy the APRS block from an old codeplug into this file during initial testing.

---

# Panduan Codeplug REV3B CLEAN

Gunakan **NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc** sebagai baseline pengujian pertama REV3B pada UV-5RM / UV-5RH **hardware Board V1**.

## Mengapa codeplug ini penting

Dalam pengujian lapangan, perilaku firmware sangat dipengaruhi konfigurasi APRS di codeplug. Salah satu codeplug lama memiliki data path APRS yang tidak konsisten dan setting lain yang membuat RX/APRS List tidak stabil. Dengan codeplug clean, firmware yang sama dapat menerima packet berulang kali tanpa reboot dan tampilan APRS Message menjadi jauh lebih konsisten.

Karena itu, laporan bug firmware sebaiknya dilakukan setelah radio terlebih dahulu diuji dengan codeplug clean ini.

## Baseline APRS clean

- APRS Ctrl: ON
- VFO A: Wide
- VFO B: Wide
- APRS bandwidth: 25K
- Tipe RX: PassAll, Position, Mic-E, Message
- Jumlah path APRS: 1
- Path APRS: WIDE2-2
- Slot path yang tidak digunakan: space-padded dengan benar
- Regular/periodic APRS send: OFF
- RX callsign filter: dikosongkan

Set callsign/SSID APRS milik pengguna setelah codeplug clean dimuat.

Untuk pengujian awal, jangan copy blok APRS dari codeplug lama ke codeplug ini.
