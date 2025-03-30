## Import modules 
import batman
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from batman import TransitParams

import os
import argparse

# Define the daneel.transit method
def daneel_transit():
    ## Parameters for exoplanet WASP-39b 
    params = batman.TransitParams()       # object to store transit parameters
    params.t0 = 0.                        # time of inferior conjunction
    params.per = 4.055259                 # orbital period
    params.rp = 0.1143                    # planet radius (in units of stellar radii)
    params.a = 11.65                      # semi-major axis (in units of stellar radii)
    params.inc = 87.83                    # orbital inclination (in degrees)
    params.ecc = 0.                       # eccentricity
    params.w = 90.                        # longitude of periastron (in degrees)

  # Calculate limb darkening coefficients from: https://exoctk.stsci.edu/limb_darkening
  # Using Kepler bandpass

  # Read the downloaded limb darkening coefficients table
  data = pd.read_csv("ExoCTK_results.txt", header=[0], delim_whitespace=True, skiprows=[1], skipfooter=30, engine='python')
  # We define the coefficients u1 and u2 as the mean of
  # coefficients c1 and c2, respectively, computed from the table.
  u1, u2 = data["c1"].mean(), data["c2"].mean()

  params.u = [u1, u2]                #limb darkening coefficients [u1, u2]
  params.limb_dark = "quadratic"     #limb darkening model

  t = np.linspace(-0.025, 0.025, 1000)  #times at which to calculate light curve

  ## Initialise model 
  m = batman.TransitModel(params, t) 

  ## Calculate the light curve 
  flux = m.light_curve(params)  

  ## Plotting the calculated light curve

  plt.figure(figsize=(8,8))
  plt.plot(t, flux, linewidth=3)
  plt.title("Transit light curve of WASP-39b", fontsize=18)
  plt.xlabel("Time [days]", fontsize=15)
  plt.ylabel("Relative flux", fontsize=15)

  # Save the plot as a PNG file
  plt.savefig("WASP_39b_assignment1_taskF.png", dpi=300)  # Adjust dpi for resolution

  # Show the plot
  plt.show()

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Exoplanet Transit Model")
    
    # Add the --transit argument to trigger the transit calculation
    parser.add_argument('-t', '--transit', action='store_true', help="Run the transit calculation")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # If -t or --transit flag is passed, call the daneel_transit method
    if args.transit:
        daneel_transit()

# If this script is run directly, execute the main function
if __name__ == "__main__":
    main()
