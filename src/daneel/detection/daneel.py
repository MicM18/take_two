import argparse
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
