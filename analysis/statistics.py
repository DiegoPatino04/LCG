import math

def gamma_pdf(x, alpha, beta):
    if x < 0:
        return 0.0
    numerator = (x ** (alpha - 1)) * math.exp(-x / beta)
    denominator = (beta ** alpha) * math.factorial(alpha - 1)
    return numerator / denominator


def gamma_cdf(x, alpha, beta):
    # Para alpha entero usamos suma de exponenciales
    if x < 0:
        return 0.0
    
    summation = 0.0
    for k in range(alpha):
        summation += (x / beta) ** k / math.factorial(k)
    
    return 1 - math.exp(-x / beta) * summation


def empirical_cdf(sorted_samples):
    n = len(sorted_samples)
    return [(i + 1) / n for i in range(n)]