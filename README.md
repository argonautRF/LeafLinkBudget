S-Band Link Budget Analysis
===========================

This repository contains two Python scripts for uplink and downlink 
S-band link budget calculations. It also includes datasheets for the 
Space Inventor STTC-P3 radio and the PATCH1-S-R antenna. The scripts 
use common link budget parameters and formulas to estimate the 
Signal-to-Noise Ratio (SNR) over varying distances (altitudes).

CONTENTS
--------
1. Overview
2. Repository Structure
3. Prerequisites
4. Scripts Explanation
   4.1. Uplink Script
   4.2. Downlink Script
5. Running the Scripts
6. Assumptions & Parameters
7. Datasheets
8. References & Further Reading

1. OVERVIEW
-----------
Satellite communication links rely on analyzing path loss, antenna 
gains, transmit power, and receiver noise levels to determine whether 
sufficient Signal-to-Noise Ratio (SNR) is achieved at different slant 
ranges. These scripts calculate:

- Free Space Path Loss (FSPL)
- Antenna Pointing Losses
- Polarization Losses
- Transmission Line Losses
- Noise Power
- Resulting SNR

Plots of SNR vs. altitude are generated to visually assess the link quality.

2. REPOSITORY STRUCTURE
-----------------------
<your-repo-name>/
  |
  +-- linkBudget_uplinkPlotting.py
  |
  +-- linkBudget_downlinkPlotting.py
  |
  +-- README.md  (this file)
  |
  +-- datasheets/
       +-- STTC-P3_Datasheet_v2.1.pdf
       +-- Single_PatchSband_Datasheet_V1.0.pdf

- linkBudget_uplinkPlotting.py: Script for uplink SNR vs. distance calculations.
- linkBudget_downlinkPlotting.py: Script for downlink SNR vs. distance calculations.
- datasheets/: PDF datasheets for the STTC-P3 radio and PATCH1-S-R antenna.

3. PREREQUISITES
----------------
- Python 3.x
- math, numpy, matplotlib (install via "pip install numpy matplotlib")

4. SCRIPTS EXPLANATION
----------------------

4.1. Uplink Script (uplink_link_budget.py)
------------------------------------------
- Defines constants (Boltzmann constant, speed of light, etc.).
- Utility functions:
  - dB_to_linear(), linear_to_dB()
  - calculate_slant_range()
  - calculate_pointing_losses()
  - calculate_extra_losses()
  - calculate_link_budget()
- Main section:
  - Sets user parameters (transmit power, gain, bandwidth, etc.).
  - Iterates over altitude range, calculates SNR, plots SNR vs. altitude.

4.2. Downlink Script (downlink_link_budget.py)
----------------------------------------------
- Similar constants and utility functions.
- Additional function calc_tsys() to derive T_sys from G and G/T (optional).
- calculate_snr() computes downlink SNR with given parameters.
- Main section:
  - Sets parameters (downlink frequency, ground station receive gain, etc.).
  - Loops over altitude range, calculates SNR, and plots SNR vs. altitude.

5. RUNNING THE SCRIPTS
----------------------
1) Clone the repository:
   git clone https://github.com/<USERNAME>/<REPO_NAME>.git
   cd <REPO_NAME>

2) Install dependencies (if needed):
   pip install numpy matplotlib

3) Run the Uplink Script:
   python uplink_link_budget.py
   This displays a plot of Uplink SNR vs. altitude.

4) Run the Downlink Script:
   python downlink_link_budget.py
   This displays a plot of Downlink SNR vs. altitude.

Uncomment the "plt.savefig(...)" line in each script if you want to 
save the plots as PNG files.

6. ASSUMPTIONS & PARAMETERS
---------------------------
- Ground Station Antenna:
  - Gains (G_tx_dBi or G_rx_dBi), HPBW, and small pointing error (e.g., 0.02 deg).
- Spacecraft Antenna:
  - Space Inventor PATCH1-S-R with assumed gain, HPBW, and 15 deg pointing error.
- Frequency:
  - Approx. 2.0 - 2.2 GHz for S-band.
- Losses:
  - 0.3 dB polarization mismatch, 0.1 dB ionosphere, 0 dB rain, 
    TX and RX transmission line losses, etc.
- Temperature:
  - System noise temperature + ambient temperature to compute noise power.
- Free Space Path Loss (FSPL):
  - FSPL(dB) = 20*log10(4*pi*distance / wavelength).
- Altitude Range:
  - Scripts vary altitude from 400 km to 60000 km.

7. DATASHEETS
-------------
- datasheets/STTC-P3-radio-datasheet.pdf
- datasheets/PATCH1-S-R-antenna-datasheet.pdf

These PDFs provide the radio and antenna specs (transmit power, gain, 
noise figure, beamwidth, etc.) used in both uplink and downlink 
calculations.

Feel free to open an issue or pull request for suggestions or improvements!
