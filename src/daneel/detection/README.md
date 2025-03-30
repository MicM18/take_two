# Daneel Transit Light Curve 

 The transit method is defined in the transit.py file and is used to generate a transit light curve.

 The parameters for the transit light curve are saved in the parameters.yaml file.

 The daneel.py file parses command-line arguments and calls the transit function.

 To call daneel:
 1) mv daneel.py /usr/local/bin/daneel
 2) chmod +x /usr/local/bin/daneel
 3) Run: daneel -i parameters.yaml -t 
