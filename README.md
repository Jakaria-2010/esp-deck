# Nexora

## ESP32-S3 Pocket Computer Project

Nexora is an open-source handheld computer built around the ESP32-S3 and CircuitPython.

Current prototype features:

- OLED graphical interface
- Phone-inspired UI navigation
- Large clock home screen
- Date and time system
- Six-button navigation
- SD-card storage
- Modular firmware architecture
- Expandable application system

## Hardware

Current prototype:

- ESP32-S3 development board
- 128x64 SSD1306 OLED (SPI)
- MicroSD card module
- Six tactile buttons

## Firmware

Location:

`firmware/circuitpython/`

Main entry:

`code.py`

Architecture:

```
code.py
 |
 +-- nexora/
     +-- boot.py
     +-- display.py
     +-- ui.py
     +-- buttons.py
     +-- clock.py
     +-- sd.py
     +-- system.py
```

## Installation

1. Install CircuitPython on ESP32-S3.
2. Copy contents of `firmware/circuitpython/` to the CIRCUITPY drive.
3. Install required libraries from `lib`.
4. Connect hardware.
5. Restart the board.

## Version

Current development version:

**Nexora v0.2.0**

## Responsible Use

Nexora is open-source. Anyone may modify and build their own version under the included licenses.

Users are responsible for their own modifications and usage. The original project contributors are not responsible for unlawful, harmful, or unauthorized use of modified versions.

## Roadmap

- Better phone-style UI
- File manager
- Music player
- Settings system
- Bluetooth features
- Custom PCB
- Enclosure design
- Stable v1.0 release

