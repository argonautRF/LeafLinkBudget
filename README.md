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
- Overview

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
