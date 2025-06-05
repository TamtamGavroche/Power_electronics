#from csv file, create plot file with the data

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#create bode plot from 2 columns in csv file and frequency column
#magnitude and phase

def plot_bode_from_csv(csv_file, output_file):
    # Read the CSV file
    data = pd.read_csv(csv_file, sep=';')
    #print("data column keys:", data.keys())

    # Check if the required columns are present
    # if 'frequency' not in data.columns or 'magnitude' not in data.columns or 'phase' not in data.columns:
    #     raise ValueError("CSV file must contain 'frequency', 'magnitude', and 'phase' columns.")

    # Extract frequency, magnitude, and phase
    frequency = data['Frequency (Hz)']
    magnitude = data['Trace 1: Gain: Magnitude (dB)']
    phase = data['Trace 2: Gain: Phase (°)']

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot magnitude
    ax1.semilogx(frequency, magnitude)
    ax1.set_title('Bode Plot - Magnitude')
    ax1.set_ylabel('Magnitude (dB)')
    ax1.grid(True)

    # Plot phase
    ax2.semilogx(frequency, phase)
    ax2.set_title('Bode Plot - Phase')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.grid(True)
    
    # Calculate the moving average with a window of window size
    window_size = 15
    magnitude_ma = magnitude.rolling(window=window_size, center=True).mean()
    phase_ma = phase.rolling(window=window_size, center=True).mean()
    # Plot the moving average on the same axes
    ax1.plot(frequency, magnitude_ma, label='Moving Average (5 points)', color='orange', linewidth=1.5)
    ax2.plot(frequency, phase_ma, label='Moving Average (5 points)', color='orange', linewidth=1.5)    

    # Save the plot to a file
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

plot_bode_from_csv('GR25_2test.csv', 'bode_plot_Q17.png')