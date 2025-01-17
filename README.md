S-Band Link Budget Analysis
===========================

This repository contains two Python scripts for uplink and downlink 
S-band link budget calculations. It also includes datasheets for the 
Space Inventor STTC-P3 radio and the PATCH1-S-R antenna. The scripts 
use common link budget parameters and formulas to estimate the 
Signal-to-Noise Ratio (SNR) over varying distances (altitudes).

Contents
--------
- Prerequisites
- Scripts Explanation
  - Uplink Script
  - Downlink Script
- Running the Scripts
- Assumptions & Parameters
- Datasheets

Prerequisites
-------------
- Python 3.x
- Required Python libraries:
  - math, numpy, matplotlib (install via: `pip install numpy matplotlib`)

Scripts Explanation
-------------------

**Uplink Script (`linkBudget_uplinkPlotting.py`)**

- Defines constants (Boltzmann constant, speed of light, etc.).
- Utility functions:
  - `dB_to_linear()`, `linear_to_dB()`
  - `calculate_slant_range()`
  - `calculate_pointing_losses()`
  - `calculate_extra_losses()`
  - `calculate_link_budget()`
- Main section:
  - Sets user parameters (transmit power, gain, bandwidth, etc.).
  - Iterates over altitude range, calculates SNR, and plots **SNR vs. altitude**.

**Downlink Script (`linkBudget_downlinkPlotting.py`)**

- Similar constants and utility functions.
- Additional function: `calc_tsys()` to derive T_sys from G and G/T (optional).
- `calculate_snr()` computes downlink SNR with given parameters.
- Main section:
  - Sets parameters (downlink frequency, ground station receive gain, etc.).
  - Loops over altitude range, calculates SNR, and plots **SNR vs. altitude**.

Assumptions
-----------
- Ground Station Antenna:
  - Gains (G_tx_dBi or G_rx_dBi), HPBW, and small pointing error 
    (e.g., 0.02 deg).
- Spacecraft Antenna:
  - Space Inventor PATCH1-S-R with assumed gain, HPBW, and a 15 deg 
    pointing error.
- Frequency:
  - Approx. 2.0 - 2.2 GHz for S-band.
- Losses:
  - 0.3 dB polarization mismatch, 0.1 dB ionosphere, 0 dB rain, and 
    combined TX/RX line losses, etc.
- Temperature:
  - System noise temperature + ambient temperature to compute noise power.
- Free Space Path Loss (FSPL):
  - FSPL(dB) = 20 * log10(4 * pi * distance / wavelength).
- Altitude Range:
  - Scripts vary altitude from 400 km to 60000 km.

Parameters
----------
- Transmit Power:
  - Uplink: 45 dBm (Leaf Space GAIA 100)
  - Downlink: 33 dBm (Space Inventor STTC-P3)
- Antenna Gains:
  - Ground Station: 35 dBi (uplink), 37.7 dBi (downlink)
  - Spacecraft: 7.5 dBi (uplink and downlink)
- Bandwidth:
  - 26.37 kHz for both uplink and downlink
- Noise Figure:
  - 5 dB (Space Inventor STTC-P3)
- Pointing Errors:
  - Ground Station: 0.02 deg
  - Spacecraft: 15 deg
- Losses:
  - Transmission Line: 4.15 dB (combined TX and RX losses)
  - Polarization: 0.3 dB
  - Ionospheric: 0.1 dB
  - Rain: 0 dB (assumed minimal at S-band)

Datasheets
----------
- STTC-P3 Radio Datasheet:
  - `datasheets/STTC-P3_Datasheet_v2.1.pdf`
- PATCH1-S-R Antenna Datasheet:
  - `datasheets/Single_PatchSband_Datasheet_V1.0.pdf`

These PDFs provide the radio and antenna specs (transmit power, gain, 
noise figure, beamwidth, etc.) used in both uplink and downlink 
calculations.
