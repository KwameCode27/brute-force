def modular_exponential(base,exponent, modular):
    result = 1
    if exponent > 0:
        result = (base*result) % modular

    return result

modular_exponential(base=7, exponent=121, )