#!/usr/bin/env python3

import argparse
import sys
import os

# Define the correct path to the original directory (to find the other files)
script_dir = "/Users/micolemiceli/Desktop/Computational_Astrophyics/take_two/src/daneel/detection"
sys.path.insert(0, script_dir)  # Add it to Python’s search path

from transit import transit

def main():
    parser = argparse.ArgumentParser(description="Daneel: Transit Light Curve Generator")
    parser.add_argument("-i", "--input", required=True, help="Path to the parameters YAML file")
    parser.add_argument("-t", "--transit", action="store_true", help="Plot the transit light curve")

    args = parser.parse_args()

    if args.transit:
        transit(args.input)

if __name__ == "__main__":
    main()
