# ESP-Deck / NexorOS v0.2.5 Hardware Wiring

## Display: SSD1306 OLED (SPI)

| OLED Pin | ESP32-S3 GPIO | Description |
|---|---:|---|
| CS | GPIO 10 | Chip Select |
| DC | GPIO 9 | Data/Command |
| RES | GPIO 8 | Reset |
| SCK | GPIO 12 | SPI Clock (shared) |
| SDA | GPIO 11 | SPI MOSI/Data (shared) |
| VCC | 3.3V | Power |
| GND | GND | Ground |

---

## SD Card Module (SPI)

| SD Pin | ESP32-S3 GPIO | Description |
|---|---:|---|
| CS | GPIO 14 | Chip Select |
| MISO | GPIO 13 | SPI Data In |
| MOSI | GPIO 11 | SPI Data Out (shared with OLED SDA) |
| CLK | GPIO 12 | SPI Clock (shared with OLED SCK) |
| VCC | 3.3V | Power |
| GND | GND | Ground |

### SPI Bus Sharing

ESP-Deck uses a shared SPI bus:

- Clock: GPIO 12
- MOSI: GPIO 11

The OLED and SD card have separate chip select pins:

- OLED CS: GPIO 10
- SD CS: GPIO 14

Only one device should be selected at a time.

---

## Navigation Buttons

Buttons use GPIO inputs.

| Button | ESP32-S3 GPIO |
|---|---:|
| Back | GPIO 16 |
| Right | GPIO 7 |
| OK / Center | GPIO 15 |
| Left | GPIO 6 |
| Up | GPIO 4 |
| Down | GPIO 5 |

---

## GPIO Summary

| Function | GPIO |
|---|---:|
| OLED CS | 10 |
| OLED DC | 9 |
| OLED RESET | 8 |
| SPI SCK | 12 |
| SPI MOSI | 11 |
| SD CS | 14 |
| SPI MISO | 13 |
| Back | 16 |
| Right | 7 |
| OK | 15 |
| Left | 6 |
| Up | 4 |
| Down | 5 |

---

## Notes

- All logic signals are 3.3V.
- Do not connect 5V signals directly to ESP32-S3 GPIO pins.
- OLED and SD card share SPI clock and MOSI lines.
- Keep wiring short and clean for reliable SPI communication.
