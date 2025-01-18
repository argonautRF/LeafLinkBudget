"""
Link Budget Analysis with Altitude Variation

Description:
This script calculates and plots the link budget margin as a function of orbital altitude for a downlink communication system.
It evaluates parameters such as free-space path loss, received power, signal-to-noise ratio (SNR), and link margin,
considering additional losses like antenna pointing losses and atmospheric attenuation.

Author: Tristan Wilson (Tristan@argospace.com)
Date: January 17, 2025
Version: 1.0

Inputs:
- Frequency (Hz)
- Transmit Power (dBm)
- Antenna Gains (dBi)
- Bandwidth (Hz)
- System Noise Temperature (K)
- Range of Orbital Altitudes (km)
- Elevation Angle (degrees)
- Additional Losses (dB)

Outputs:
- Link Margin vs Altitude Plot

Dependencies:
- Python 3.x
- NumPy
- Matplotlib

Usage:
- Modify user-defined parameters as needed.
- Run the script to generate the plot.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 1.38064852e-23  # Boltzmann constant (J/K)
c = 299792458         # Speed of light (m/s)

# Utility Functions
def dB_to_linear(dB):
    return 10 ** (dB / 10)

def linear_to_dB(linear):
    return 10 * math.log10(linear)

def calculate_slant_range(earth_radius_km, orbit_altitude_km, elevation_angle_deg):
    elevation_angle_rad = math.radians(elevation_angle_deg)
    earth_radius_m = earth_radius_km * 1e3
    orbit_radius_m = (earth_radius_km + orbit_altitude_km) * 1e3

    slant_range_m = earth_radius_m * (
        (((orbit_radius_m ** 2 / earth_radius_m ** 2) - (math.cos(elevation_angle_rad)) ** 2) ** 0.5) -
        math.sin(elevation_angle_rad)
    )
    return slant_range_m

def calc_tsys(G_dB, GT_dB):
    T_sys = 10 ** (G_dB / 10) / 10 ** (GT_dB / 10)
    return T_sys

def calculate_pointing_losses(gs_pointError, sc_pointError, gs_antHPBW, sc_antHPBW):
    gs_rollOff = 2 * (gs_pointError * (79.76 / gs_antHPBW))
    gs_pointLoss_dB = -10 * math.log10(3282.81 * ((math.sin(math.radians(gs_rollOff)) ** 2) / (gs_rollOff ** 2)))

    sc_rollOff = 12 * (sc_pointError / sc_antHPBW) ** 2
    sc_pointLoss_dB = sc_rollOff

    return gs_pointLoss_dB + sc_pointLoss_dB

def calculate_extra_losses(ant_pointLoss, polLoss, ionLoss, atmLoss, rainLoss, tLineLoss):
    return ant_pointLoss + polLoss + ionLoss + atmLoss + rainLoss + tLineLoss

def calculate_snr(frequency_Hz, distance_m, P_tx_dBm, G_tx_dBi, G_rx_dBi, bandwidth_Hz, T, extraLoss):
    wavelength_m = c / frequency_Hz
    FSPL_dB = 20 * math.log10(4 * math.pi * distance_m / wavelength_m)

    EIRP_dBm = P_tx_dBm + G_tx_dBi
    P_rx_dB = EIRP_dBm + G_rx_dBi - FSPL_dB - extraLoss

    noise_power_dB = linear_to_dB(k_B * T * bandwidth_Hz) + 30
    SNR_dB = P_rx_dB - noise_power_dB

    return SNR_dB

# assuming Leaf Space LEGION 400/400T
G_rx_dBi = 37.7 # dBi
T_sys = 130.13 # Kelvin
T_a = 50 # Kelvin, please double-check this assumption
T = T_a + T_sys
gs_pointError = 0.02 # deg, antenna pointing error
gs_antHPBW = 2.115 # deg, antenna half-power beamwidth

# Parameters
frequency_Hz = 2.2e9 # Hz, depends on licensing - assumed for analysis
elevation_angle_deg = 45 # deg, assumed value
G_tx_dBi = 7 # dBi, Space Inventor STTC-P3
bandwidth_Hz = 26.37e3 # Hz, matched to TX bandwidth
P_tx_dBm = 33 # dBm, max transmit power from Space Inventor STTC-P3

# on spacecraft
# assuming Space Inventor PATCH1-S-R patch antenna
sc_pointError = 15 # deg, assumed
sc_antHPBW = 86 # deg, Space Inventor PATCH1-S-R

# assumed losses
polLoss = 0.3 # dB, polarization mismatch losses (circular pol at spacecraft to circular pol at ground)
atmLoss = 0.3 # dB, loss due to atmospheric gases
ionLoss = 0.1 # dB, loss due to ionosphere (minimal at S-Band)
rainLoss = 0 # dB, loss from rain (not factored in - link margin accounts for bad weather conditions)
TX_electronicsLoss = 3.65 # dB, from circuitry at output of spacecraft radio
RX_electronicsLoss = 0.5 # dB, NOT CERTAIN ABOUT THIS
tLineLoss = TX_electronicsLoss + RX_electronicsLoss

# calculation
# Antenna pointing losses
ant_pointLoss = calculate_pointing_losses(gs_pointError, sc_pointError, gs_antHPBW, sc_antHPBW)

# calculation
# Additional losses (dB)
extraLoss = calculate_extra_losses(ant_pointLoss, polLoss, atmLoss, ionLoss, rainLoss, tLineLoss)

earth_radius_km = 6378.14 # km
altitudes = np.linspace(400, 60000, 500)  # Altitudes from 400 km to 60,000 km
snrs = []

for altitude in altitudes:
    slant_range_m = calculate_slant_range(earth_radius_km, altitude, elevation_angle_deg)
    snr = calculate_snr(frequency_Hz, slant_range_m, P_tx_dBm, G_tx_dBi, G_rx_dBi, bandwidth_Hz, T, extraLoss)
    snrs.append(snr)

plt.style.use("dark_background")
plt.figure(figsize=(10, 6))
plt.plot(altitudes, snrs, label='SNR', color='cyan', linewidth=2)

# Add horizontal lines for SNR thresholds
plt.axhline(y=12, color='green', linestyle='--', label='6dB SNR with 6dB Margin')
plt.axhline(y=9, color='yellow', linestyle='--', label='6dB SNR with 3dB Margin')
plt.axhline(y=6, color='red', linestyle='--', label='6dB SNR')

plt.xlabel('Distance from Ground Station (km)', fontsize=12, color='white')
plt.ylabel('SNR (dB)', fontsize=12, color='white')
plt.title('Downlink SNR vs Distance', fontsize=14, color='white', pad=15)
plt.xlim(400, 60000)
plt.ylim(0, 60)  # Adjusted for typical SNR ranges
plt.grid(which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.minorticks_on()
plt.legend(loc='upper right', fontsize=10)
# plt.savefig('downlink_snr_vs_altitude.png', dpi=300, bbox_inches='tight')
plt.show()