# REV3B CLEAN / NUSA 3B — Board V1 APRS Message + Clean Codeplug

## English

**REV3B CLEAN / NUSA 3B** is the consolidated APRS build for **Baofeng UV-5RM / UV-5RH hardware Board V1** using the V2.0.9 firmware family.

### Download both files

Use the firmware **together with the supplied clean codeplug**:

- `NUSA_UV5RH_BOARDV1_REV3B_CLEAN_APRS_MESSAGE.dat`
- `NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc`

Do not reuse an old or unknown codeplug for first testing. During development, malformed/legacy APRS settings were found to cause empty APRS List entries, unstable receive behavior, and misleading test results.

### What has been verified

The functional REV3A logic that REV3B CLEAN preserves was tested on Board V1 and displayed APRS Message bodies of **18, 19, 20 and 24 characters** when the RF channel was clear. This proves reception beyond the first 19-byte display chunk.

The APRS Message TX path is the OEM type-6 / Message builder path. The same relevant TX path was field-tested over RF using a Board V1 REV2S sender and successfully delivered APRS Messages to the receiving radio.

The Long-SK2 manual beacon path retained in REV3B comes from REV2V, whose OEM-queue manual beacon was separately field-tested over RF.

REV3B differs from the successful REV3A binary only by the displayed version label `NUSA 3A -> NUSA 3B`; no functional instruction or data path was changed for the clean release.

### Main APRS behavior

- Bell-202 / AX.25 APRS receive retained.
- APRS Message/SMS addressed to the configured local APRS callsign can be accepted and displayed.
- Safe APRS List detail rendering is retained to avoid walking beyond valid display chunks.
- Long Message body handling is retained from the successful REV3A logic.
- OEM APRS Message TX path is retained.
- Long SK2 manual beacon uses the field-tested REV2V OEM queue/state-machine method.
- Normal FM RX/TX, GNSS and normal radio operation are retained.

### Required / recommended codeplug

The included `NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc` is the recommended baseline.

Important APRS configuration in this clean codeplug:

- APRS Ctrl: **ON**
- VFO A/B bandwidth: **Wide**
- APRS bandwidth: **25K**
- Receive packet types enabled for clean testing: **PassAll + Position + Mic-E + Message**
- APRS path count: **1**
- Path: **WIDE2-2**
- Unused path entries are space-padded, not malformed NUL callsigns.
- Periodic/regular APRS send: **OFF**
- RX callsign filter list: cleared for clean testing.

After loading the codeplug, change only station-specific values such as your own APRS source callsign/SSID and other intentional user settings. Avoid importing APRS settings from an old codeplug until the radio has first been verified with this clean baseline.

### Board compatibility

- **Board V1:** REV3B CLEAN is intended for this hardware revision.
- **Board V2:** continue using **REV2K**. Do not flash REV3B to Board V2 unless separately verified.
- Keep known-good stock/recovery firmware available.

### Checksums

Firmware SHA-256:

`4f1d6c6346a46964eb45806fdc3e52e49dcb358b0c455b3678c7e86522b791d6`

Codeplug SHA-256:

`c8c0ca836718987108a73adddca1b5ae23ff5af6daca04ea59e2bc494f5073af`

---

## Bahasa Indonesia

**REV3B CLEAN / NUSA 3B** adalah build APRS bersih/terkonsolidasi untuk **Baofeng UV-5RM / UV-5RH hardware Board V1** yang memakai keluarga firmware V2.0.9.

### Download dan gunakan kedua file

Gunakan firmware **bersama codeplug clean yang disediakan**:

- `NUSA_UV5RH_BOARDV1_REV3B_CLEAN_APRS_MESSAGE.dat`
- `NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc`

Untuk pengujian pertama, jangan memakai codeplug lama atau codeplug yang asal-usulnya tidak jelas. Pada proses pengembangan ditemukan bahwa konfigurasi APRS/codeplug lama yang tidak bersih dapat menyebabkan APRS List kosong, RX tidak stabil, atau membuat hasil pengujian terlihat seperti bug firmware.

### Yang sudah terbukti

Logic REV3A yang dipertahankan byte-for-byte oleh REV3B CLEAN telah diuji pada Board V1 dan berhasil menampilkan isi APRS Message **18, 19, 20 dan 24 karakter** ketika kanal RF sepi. Artinya penerimaan message sudah terbukti melewati batas chunk pertama 19 byte.

Jalur TX APRS Message menggunakan jalur OEM task type-6 / Message builder. Jalur TX relevan yang sama telah diuji lewat RF menggunakan UV-5RH Board V1 REV2S sebagai pengirim dan pesan berhasil diterima radio tujuan.

Manual beacon Long-SK2 pada REV3B mempertahankan metode OEM queue/state-machine dari REV2V yang sebelumnya sudah diuji benar-benar memancar melalui RF.

REV3B hanya berbeda dari binary REV3A yang berhasil diuji pada label tampilan `NUSA 3A -> NUSA 3B`; tidak ada instruksi fungsi atau jalur data yang diubah untuk rilis clean ini.

### Perilaku APRS utama

- RX APRS Bell-202 / AX.25 dipertahankan.
- APRS Message/SMS ke callsign APRS lokal dapat diterima dan ditampilkan.
- Safe renderer APRS List/detail dipertahankan untuk mencegah pembacaan chunk di luar batas.
- Penanganan body Message panjang mempertahankan logic REV3A yang berhasil diuji.
- Jalur OEM TX APRS Message dipertahankan.
- Long SK2 manual beacon memakai metode OEM queue REV2V yang sudah teruji.
- FM RX/TX normal, GNSS dan fungsi radio normal tetap dipertahankan.

### Codeplug yang harus dijadikan baseline

Gunakan `NUSA_REV3B_BOARDV1_CLEAN_SAFE.xlc` sebagai baseline yang direkomendasikan.

Konfigurasi APRS penting pada codeplug clean:

- APRS Ctrl: **ON**
- Bandwidth VFO A/B: **Wide**
- APRS bandwidth: **25K**
- Tipe RX untuk tes clean: **PassAll + Position + Mic-E + Message**
- Jumlah path: **1**
- Path: **WIDE2-2**
- Slot path yang tidak dipakai diisi space dengan benar, bukan callsign NUL yang malformed.
- Periodic/regular APRS send: **OFF**
- RX callsign filter: dikosongkan untuk pengujian clean.

Setelah codeplug dimuat, ubah hanya nilai yang memang khusus stasiun pengguna seperti APRS source callsign/SSID serta setting lain yang sengaja diperlukan. Jangan langsung mengimpor setting APRS dari codeplug lama sebelum radio terbukti normal dengan baseline clean ini.

### Kompatibilitas board

- **Board V1:** gunakan REV3B CLEAN.
- **Board V2:** tetap gunakan **REV2K**.
- Selalu simpan firmware stock/recovery yang sudah terbukti bekerja.

### Checksum

Firmware SHA-256:

`4f1d6c6346a46964eb45806fdc3e52e49dcb358b0c455b3678c7e86522b791d6`

Codeplug SHA-256:

`c8c0ca836718987108a73adddca1b5ae23ff5af6daca04ea59e2bc494f5073af`
