# ESP-Deck

## NexorOS — the operating system of ESP-Deck

**ESP-Deck** is an open-source ESP32-S3 handheld platform designed for embedded
experimentation, hardware learning, system utilities, and authorized security
research.

The operating system is called **NexorOS**.

NexorOS is being developed as a modular handheld OS: a small graphical system
that can grow from the current clock/UI prototype into a collection of
applications and hardware tools.

> **Current status:** Prototype / active development  
> **Current firmware milestone:** v0.2.5

## Project identity

| Name | Meaning |
|---|---|
| **ESP-Deck** | The handheld device/platform and GitHub repository |
| **NexorOS** | The operating system running on ESP-Deck |
| **Nexor** | Project-family naming convention used for future projects |

The name **Nexor** is a project naming concept associated with the idea of a
“next core” engineering platform. This repository does **not** make any claim
that the name is unique, legally available as a trademark, or available in
every jurisdiction. Perform appropriate trademark/name checks before using
Nexor or NexorOS commercially.

## Current prototype

The v0.2.5 prototype includes:

- ESP32-S3 platform
- SSD1306 SPI OLED interface
- Large clock and date home screen
- Physical six-button navigation
- SD-card storage
- Modular CircuitPython firmware
- Phone-inspired UI layout
- NexorOS branding

## Hardware

### OLED — SSD1306 SPI

| Function | GPIO |
|---|---:|
| CS | GPIO 10 |
| DC | GPIO 9 |
| RESET | GPIO 8 |
| SCK | GPIO 12 |
| MOSI / SDA | GPIO 11 |

### SD card — SPI

| Function | GPIO |
|---|---:|
| CS | GPIO 14 |
| MISO | GPIO 13 |
| MOSI | GPIO 11 |
| CLK | GPIO 12 |

The OLED and SD card share the SPI clock and MOSI lines. They use separate
chip-select pins.

### Buttons

| Button | GPIO |
|---|---:|
| Back | GPIO 16 |
| Right | GPIO 7 |
| OK / Center | GPIO 15 |
| Left | GPIO 6 |
| Up | GPIO 4 |
| Down | GPIO 5 |

See [`hardware/wiring/nexora_wiring.md`](hardware/wiring/nexora_wiring.md) and
[`hardware/pinout.md`](hardware/pinout.md).

## Repository structure

```text
esp-deck/
├── README.md
├── LICENSE
├── LICENSE-MIT.txt
├── LICENSE-CERN-OHL-S-2.0.txt
├── LICENSE-CC-BY-4.0.txt
├── NOTICE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── .gitignore
│
├── firmware/
│   └── circuitpython/
│       ├── code.py
│       ├── nexora/
│       ├── lib/
│       └── font5x8.bin
│
├── hardware/
│   ├── README.md
│   ├── pinout.md
│   ├── wiring/
│   ├── schematics/
│   └── pcb/
│
├── tools/
│   ├── README.md
│   ├── ir/
│   └── wifi/
│
├── docs/
│   ├── architecture.md
│   ├── branding.md
│   ├── security-model.md
│   └── release-process.md
│
├── assets/
│   ├── photos/
│   ├── screenshots/
│   └── video/
│
└── examples/
```

## Advanced tools

ESP-Deck is intended to host optional hardware/security-research tools.
Examples include IR experimentation and Wi-Fi security research.

These tools are intended for **equipment, networks, devices, and environments
that you own or have explicit permission to test**. The project does not
authorize unauthorized access, credential theft, disruption, or interception.

Tool documentation is kept separate from the core NexorOS system so that
experimental features can evolve without destabilizing the base OS.

See [`tools/README.md`](tools/README.md).

## Firmware

The firmware is written in CircuitPython.

The Python package directory is currently named `nexora/` for compatibility
with the existing v0.2.5 codebase. The user-facing operating-system name is
**NexorOS**.

This distinction allows the branding to change without unnecessarily breaking
existing imports or SD-card data.

## Development

ESP-Deck is an active prototype. Hardware, UI, APIs, and tool interfaces may
change.

Recommended workflow:

```text
Develop → Test on hardware → Commit → Push → Tag → Release
```

Keep experimental features on branches and keep `main` in a usable state.

## Safety and responsible use

ESP-Deck is a general-purpose embedded platform. Some future tools may have
dual-use capabilities.

Users are responsible for:
- their hardware modifications;
- their firmware modifications;
- their network and radio environments;
- obtaining permission before security testing;
- complying with applicable laws and regulations.

See [`SECURITY.md`](SECURITY.md) and [`docs/security-model.md`](docs/security-model.md).

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before
opening a pull request.

## Roadmap

### NexorOS
- [x] Boot/home screen
- [x] Clock and date
- [x] Button navigation
- [x] SD-card foundation
- [ ] Application launcher
- [ ] File manager
- [ ] Settings
- [ ] System information
- [ ] Power-management improvements

### ESP-Deck tools
- [ ] IR laboratory / learning tools
- [ ] Wi-Fi security-research tools
- [ ] Additional hardware diagnostics
- [ ] Modular tool permissions/safety model

### Hardware
- [ ] Cleaner prototype wiring
- [ ] Custom PCB
- [ ] Enclosure
- [ ] Power subsystem refinement

## License

Different project components use different licenses:

- Firmware/software: **MIT**
- Hardware design: **CERN-OHL-S-2.0**
- Documentation and original media: **CC BY 4.0**

See the individual license files and [`NOTICE.md`](NOTICE.md).

---

**ESP-Deck — hardware platform. NexorOS — operating system.**
