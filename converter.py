def convert(feet, inches):
    meters = (feet * 30.48)/100 + (inches * 2.54)/100
    return meters
