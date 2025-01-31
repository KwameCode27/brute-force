def modular_exponential(base,exponent, modular):
    result = 0
    if exponent > 0:
        result = (base*exponent) % modular

    return result

