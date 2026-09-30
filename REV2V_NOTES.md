# REV2V / NUSA 2V — Board V1 Manual APRS Beacon

## English

REV2V / **NUSA 2V** is a field-tested feature release for **Baofeng UV-5RM / UV-5RH Board V1** units that use the V2.0.9 firmware family.

**Board V1 development baseline remains REV2R / NUSA 2R.** REV2V is built directly from that baseline and adds the corrected manual-beacon trigger.

### Field-confirmed manual beacon

**Long SK2 / PF2 → one manual APRS beacon over RF.**

REV2S previously called the APRS/Bell-202 builder directly from the key event. Field testing showed that this could produce local AFSK audio without actually keying RF.

REV2V fixes this by routing Long SK2 through the **OEM APRS beacon request / queue / radio state machine**. The OEM path performs the radio-state and RF-TX preparation before the APRS frame is transmitted.

Field testing on Board V1 has confirmed that the manual beacon now transmits correctly over RF.

### Behavior

- APRS Ctrl **ON** + Long SK2 → request one OEM APRS beacon.
- APRS Ctrl **OFF** + Long SK2 → no beacon TX.
- Other key events continue through the OEM dispatcher.
- APRS RX/TX modem behavior inherited from REV2R is unchanged.
- APRS List/detail, GNSS, backlight, normal FM RX/TX, RF gain/LNA/PGA/AGC and squelch are not changed by the REV2V manual-beacon patch.

### Board compatibility

- **Board V1:** REV2V / NUSA 2V is the latest field-tested feature release.
- **Board V1 baseline:** REV2R / NUSA 2R remains the development/recovery baseline.
- **Board V2:** continue using **REV2K**. Do not use REV2V on Board V2 unless separately verified.

Firmware:

`NUSA_UV5RH_BOARDV1_REV2V_MANUAL_BEACON_OEM_QUEUE.dat`

SHA-256:

`744352003e74f39d0dfe2d53126a7bd29be09c0c7ad130708489dd12143939b4`

---

## Bahasa Indonesia

REV2V / **NUSA 2V** adalah rilis fitur yang sudah diuji di lapangan untuk **Baofeng UV-5RM / UV-5RH Board V1** yang menggunakan keluarga firmware V2.0.9.

**Basis pengembangan Board V1 tetap REV2R / NUSA 2R.** REV2V dibuat langsung dari baseline tersebut dan menambahkan trigger manual beacon yang sudah diperbaiki.

### Manual beacon sudah terkonfirmasi

**Long SK2 / PF2 → satu APRS beacon benar-benar terpancar melalui RF.**

Pada REV2S, Long SK2 memanggil builder APRS/Bell-202 secara langsung. Hasil pengujian menunjukkan audio AFSK dapat terdengar di speaker tetapi RF belum benar-benar TX.

REV2V memperbaikinya dengan memasukkan permintaan Long SK2 melalui **jalur OEM APRS beacon queue / radio state machine**. Jalur OEM inilah yang menyiapkan kondisi radio dan RF TX sebelum frame APRS dikirim.

Pengujian langsung pada Board V1 sudah mengonfirmasi bahwa manual beacon REV2V **memancar RF dengan baik**.

### Perilaku

- APRS Ctrl **ON** + Long SK2 → meminta satu APRS beacon melalui jalur OEM.
- APRS Ctrl **OFF** + Long SK2 → tidak TX beacon.
- Event tombol lainnya tetap memakai dispatcher OEM.
- Modem APRS RX/TX dari REV2R tidak diubah.
- APRS List/detail, GNSS, backlight, FM RX/TX biasa, RF gain/LNA/PGA/AGC dan squelch tidak diubah oleh patch manual-beacon REV2V.

### Kompatibilitas board

- **Board V1:** REV2V / NUSA 2V adalah feature release terbaru yang sudah diuji.
- **Baseline Board V1:** REV2R / NUSA 2R tetap menjadi basis pengembangan/recovery.
- **Board V2:** tetap gunakan **REV2K**. Jangan memakai REV2V pada Board V2 sebelum ada pengujian terpisah.
