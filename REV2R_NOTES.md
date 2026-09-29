# REV2R / NUSA 2R — APRS Ctrl Fix + RX/TX Compatibility

## English

REV2R is intended for **Baofeng UV-5RM / UV-5RH board V1** radios that are already known to accept the **V2.0.9 firmware family**. It is based on the stable REV2K branch and carries forward the APRS modem compatibility work from REV2P/REV2Q.

> **Board warning:** the `V2` wording in the project/file history refers to the **V2.0.9 firmware family**, not a board-V2 hardware revision. Do not flash this build to board V2/V3 or another hardware revision unless compatibility has been independently confirmed.

### Confirmed field results

- TX/beacon compatibility improved: packets were successfully digipeated by VP-Digi and TYT during REV2P testing.
- APRS List and packet-detail display remain available.
- Firmware version shown on the radio is shortened to **NUSA 2R**.
- **APRS → APRS Ctrl → OFF is confirmed working on the radio in REV2R.**

### RX changes retained

- Bell-202 timing recovery correction widened to ±0x20.
- SPACE correlator weighting +25%.
- Weak-signal tone decision uses the REV2Q zero-floor decision.
- Normal AX.25/HDLC and CRC/FCS validation remain active.

### TX changes retained

- Bell-202 timing correction toward nominal 1200 baud.
- AX.25 address reserved bits corrected to 0x60.

### Important

REV2R does **not** apply speculative RF sensitivity/LNA/PGA/AGC register modifications. The weak-signal RX improvements still require continued field testing at low RF levels.

---

## Bahasa Indonesia

REV2R ditujukan untuk **Baofeng UV-5RM / UV-5RH board V1** yang sudah terbukti dapat menggunakan **keluarga firmware V2.0.9**. REV2R berbasis cabang stabil REV2K dan mempertahankan perbaikan kompatibilitas modem APRS dari REV2P/REV2Q.

> **Peringatan board:** istilah `V2` pada riwayat project/nama file mengacu pada **keluarga firmware V2.0.9**, bukan hardware board V2. Jangan flash firmware ini ke board V2/V3 atau revisi hardware lain kecuali kompatibilitasnya sudah terverifikasi.

### Hasil pengujian lapangan yang sudah terkonfirmasi

- Kompatibilitas TX/beacon membaik: packet berhasil didigipeat oleh VP-Digi dan TYT pada pengujian REV2P.
- APRS List dan tampilan detail packet tetap dipertahankan.
- Versi firmware yang tampil di radio menggunakan teks pendek **NUSA 2R**.
- **APRS → APRS Ctrl → OFF sudah terkonfirmasi berfungsi pada REV2R.**

### Perbaikan RX yang dipertahankan

- Koreksi timing recovery Bell-202 diperlebar menjadi ±0x20.
- Bobot correlator SPACE +25%.
- Keputusan tone weak-signal memakai zero-floor dari REV2Q.
- Validasi AX.25/HDLC dan CRC/FCS tetap aktif.

### Perbaikan TX yang dipertahankan

- Koreksi timing Bell-202 menuju nominal 1200 baud.
- Reserved bits alamat AX.25 diperbaiki menjadi 0x60.

### Penting

REV2R **tidak** memakai perubahan spekulatif pada register RF sensitivity/LNA/PGA/AGC. Peningkatan RX sinyal lemah masih perlu dilanjutkan dengan pengujian lapangan pada level RF rendah.

## Firmware

`NUSA_UV5RH_PRO_V2_REV2R_APRS_CTRL_FIX_BOARDV1.dat`

SHA-256:

`03e8a3a47dd2f133112013261db83e4b201062cc9b519fc909427d949670276d`
