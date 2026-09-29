# NUSA UV-5RH PRO V2 APRS Firmware

Custom APRS firmware for **Baofeng UV-5RM / UV-5RH board V1** that is compatible with the **V2.0.9 firmware family**.

Current firmware files:

- `NUSA_UV5RH_PRO_V2_REV2K_APRS_PACKET_DETAIL.dat` — stable APRS packet-detail baseline
- `NUSA_UV5RH_PRO_V2_REV2R_APRS_CTRL_FIX_BOARDV1.dat` — current NUSA 2R compatibility build

## Latest development: REV2R / NUSA 2R

REV2R is the current compatibility build for **UV-5RM / UV-5RH board V1** radios that use the V2.0.9 firmware family. It retains the REV2P/REV2Q APRS modem compatibility changes while restoring the OEM APRS enable/disable control. Field testing has confirmed that **APRS → APRS Ctrl → OFF now works correctly**. TX/beacon compatibility improvements from REV2P were also confirmed with VP-Digi and TYT. Weak-signal RX remains an active field-test area; no speculative RF gain/LNA/PGA/AGC register changes are used.

See `REV2R_NOTES.md` for bilingual details.

> **BOARD COMPATIBILITY — IMPORTANT:** REV2R / NUSA 2R is intended for **Baofeng UV-5RM / UV-5RH board V1** units that are already known to accept the **V2.0.9 firmware family**. The `V2` wording in the project/file history refers to the **V2.0.9 firmware family**, not to a board-V2 hardware revision. **Do not flash REV2R to a different board/hardware revision unless compatibility has been independently confirmed.**

---

## English

### Overview

REV2K is a stability-focused APRS receive build for the Baofeng UV-5RH PRO V2. It was developed from the V2.0.9 firmware family and keeps the normal radio functions while improving the APRS receive/list/detail path.

### Main features

- APRS Bell 202 / AX.25 receive support.
- APRS List reception retained.
- Received station callsign can be shown in the APRS interface.
- APRS packet details can be opened from the APRS List using MENU/Confirm.
- Position packet handling retained.
- Mic-E packet handling retained.
- Normal FM radio operation retained.
- Existing V2-series backlight correction retained.
- Designed as the stable base for further NUSA APRS development.

### Field-test status

REV2K has been tested on compatible UV-5RH PRO V2 hardware and is the stable reference build used for continued development. During testing, APRS packets could be received, stations appeared in APRS List, and packet/station detail could be opened without the hang/reboot behavior seen in several earlier experimental builds.

### Known limitations

- APRS message/SMS receive is **not considered solved in REV2K**. Message receive work is being developed separately.
- APRS Object detail support is not complete in REV2K.
- REV2K is **not a digipeater** and **not an iGate**.
- Do not assume compatibility with UV-5RH/5RM hardware revisions that use a different firmware architecture.

### Compatibility

Target:

- **Baofeng UV-5RM / UV-5RH board V1**.
- Unit must already be compatible with the **V2.0.9 firmware family**.
- Firmware package size: 401,488 bytes.

**Not intended for unverified board V2/V3 or other hardware revisions.**

This project must not be treated as interchangeable with UV-K5 or other BK4819-based projects. The UV-5RH PRO exists in multiple hardware/firmware variants.

### Flashing / recovery

Keep a known-good original V2.0.9 firmware file available before flashing any experimental firmware.

Recommended checks after flashing:

1. Verify normal boot.
2. Verify FM RX and TX.
3. Verify keypad and menu operation.
4. Verify APRS RX.
5. Open APRS List and packet detail.

If the receiver behaves abnormally after testing another experimental build, perform a **Factory Reset / Reset ALL** before concluding that the radio hardware is damaged. During development, a receiver state/configuration problem was successfully recovered by factory reset.

### Warning

Custom firmware is experimental and flashing is performed at the user's own risk. Always keep a known-good recovery firmware and use the correct updater procedure for the exact hardware revision.

---

## Bahasa Indonesia

### Gambaran Umum

REV2K adalah firmware APRS yang berfokus pada kestabilan penerimaan untuk **Baofeng UV-5RH PRO V2**. Firmware ini dikembangkan dari keluarga firmware V2.0.9 dan mempertahankan fungsi radio normal sambil memperbaiki jalur penerimaan, APRS List, dan tampilan detail packet APRS.

### Fitur utama

- Mendukung penerimaan APRS Bell 202 / AX.25.
- APRS List tetap berfungsi.
- Callsign stasiun yang diterima dapat tampil pada antarmuka APRS.
- Detail packet/stasiun dapat dibuka dari APRS List menggunakan MENU/Confirm.
- Penerimaan packet posisi tetap dipertahankan.
- Penerimaan Mic-E tetap dipertahankan.
- Fungsi radio FM normal tetap dipertahankan.
- Perbaikan backlight dari seri V2 tetap dipertahankan.
- Digunakan sebagai basis stabil untuk pengembangan firmware NUSA APRS berikutnya.

### Status pengujian lapangan

REV2K telah diuji pada hardware UV-5RH PRO V2 yang kompatibel dan menjadi firmware referensi stabil untuk pengembangan lanjutan. Dalam pengujian, packet APRS dapat diterima, stasiun dapat muncul di APRS List, dan detail packet/stasiun dapat dibuka tanpa gejala hang/reboot seperti yang terjadi pada beberapa build eksperimen sebelumnya.

### Keterbatasan yang diketahui

- Penerimaan **APRS Message/SMS belum dianggap selesai pada REV2K**. Perbaikannya dikembangkan terpisah.
- Detail APRS Object belum lengkap pada REV2K.
- REV2K **bukan digipeater** dan **bukan iGate**.
- Jangan menganggap firmware ini kompatibel dengan semua revisi UV-5RH/5RM karena terdapat beberapa varian hardware dan arsitektur firmware yang berbeda.

### Kompatibilitas

Target:

- **Baofeng UV-5RM / UV-5RH board V1**.
- Unit harus sudah terbukti kompatibel dengan **keluarga firmware V2.0.9**.
- Ukuran paket firmware: 401.488 byte.

**Tidak ditujukan untuk board V2/V3 atau revisi hardware lain yang belum terverifikasi.**

Proyek ini tidak boleh dianggap sama dengan proyek UV-K5 atau perangkat BK4819 lain tanpa verifikasi. UV-5RH PRO memiliki beberapa varian hardware/firmware.

### Flashing / recovery

Sebelum mencoba firmware modifikasi, selalu simpan firmware original V2.0.9 yang sudah terbukti dapat digunakan untuk recovery.

Pemeriksaan yang disarankan setelah flashing:

1. Pastikan radio boot normal.
2. Tes RX dan TX FM biasa.
3. Tes keypad dan menu.
4. Tes penerimaan APRS.
5. Buka APRS List dan detail packet.

Jika RX menjadi abnormal setelah mencoba firmware eksperimen lain, lakukan **Factory Reset / Reset ALL** terlebih dahulu sebelum menyimpulkan bahwa hardware radio rusak. Pada proses pengembangan, kondisi receiver yang bermasalah berhasil dipulihkan dengan factory reset.

### Peringatan

Firmware custom bersifat eksperimental dan proses flashing dilakukan dengan risiko pengguna sendiri. Selalu simpan firmware recovery yang sudah terbukti baik dan gunakan prosedur updater yang sesuai dengan revisi hardware radio.

---

## Files

- `NUSA_UV5RH_PRO_V2_REV2K_APRS_PACKET_DETAIL.dat` — firmware REV2K stable baseline
- `NUSA_UV5RH_PRO_V2_REV2R_APRS_CTRL_FIX_BOARDV1.dat` — firmware REV2R / display `NUSA 2R`
- `REV2R_NOTES.md` — REV2R bilingual notes

## Project status

REV2K is kept as the **stable APRS packet-detail baseline**. New experimental features should be developed in separate revisions so that this build remains available as a recovery/reference point.

REV2K dipertahankan sebagai **baseline stabil APRS packet-detail**. Fitur eksperimen baru sebaiknya dikembangkan pada revisi terpisah agar build ini tetap tersedia sebagai titik referensi/recovery.
