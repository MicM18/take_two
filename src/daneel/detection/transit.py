import batman
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import argparse
import yaml  # Import the YAML module for loading parameter files

from batman import TransitParams

# Define the daneel.transit method
def transit(parameter_file):
    ## Read parameters from YAML file
    with open(parameter_file, 'r') as file:
        params_dict = yaml.safe_load(file)
    
    # Initialize the parameters from the YAML file
    params = batman.TransitParams() 
    params.t0 = params_dict['t0']  # time of inferior conjunction
    params.per = params_dict['per']  # orbital period
    params.rp = params_dict['rp']  # planet radius
    params.a = params_dict['a']  # semi-major axis
    params.inc = params_dict['inc']  # orbital inclination
    params.ecc = params_dict['ecc']  # eccentricity
    params.w = params_dict['w']  # longitude of periastron

    # Check if the limb darkening file exists
    ld_file = "ExoCTK_results.txt"
    if not os.path.exists(ld_file):
        raise FileNotFoundError(f"The limb darkening coefficients file {ld_file} was not found. Please ensure the file is in the correct location.")

    # Read the downloaded limb darkening coefficients table
    data = pd.read_csv(ld_file, header=[0], delim_whitespace=True, skiprows=[1], skipfooter=30, engine='python')

    # We define the coefficients u1 and u2 as the mean of coefficients c1 and c2, respectively, computed from the table.
    u1, u2 = data["c1"].mean(), data["c2"].mean()

    params.u = [u1, u2]  # limb darkening coefficients
    params.limb_dark = "quadratic"  # limb darkening model

    t = np.linspace(-0.025, 0.025, 1000)  # times at which to calculate light curve

    ## Initialise model 
    m = batman.TransitModel(params, t) 

    ## Calculate the light curve 
    flux = m.light_curve(params)  

    ## Plotting the calculated light curve
    plt.figure(figsize=(8,8))
    plt.plot(t, flux, linewidth=3)
    plt.title(f"Transit light curve of {params_dict['planet_name']}", fontsize=18)
    plt.xlabel("Time [days]", fontsize=15)
    plt.ylabel("Relative flux", fontsize=15)

    # Save the plot as a PNG file
    plt.savefig(f"{params_dict['planet_name']}_light_curve.png", dpi=300)  # Save with planet name

    # Show the plot
    plt.show()
