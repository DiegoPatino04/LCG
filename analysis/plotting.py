import matplotlib.pyplot as plt
import numpy as np
from analysis.statistics import gamma_pdf, gamma_cdf, empirical_cdf

def plot_histogram_with_pdf(samples, alpha, beta, bins):
    plt.figure(figsize=(10,6))
    
    # Histograma empírico
    counts, bin_edges, _ = plt.hist(samples, bins=bins, density=True, alpha=0.6, label="Empirical")

    # Curva teórica
    x = np.linspace(0, max(samples), 1000)
    y = [gamma_pdf(val, alpha, beta) for val in x]

    plt.plot(x, y, 'r', label="Theoretical PDF")
    plt.title(f"Gamma Distribution (α={alpha}, β={beta})")
    plt.legend()
    plt.show()


def plot_cdf_comparison(samples, alpha, beta):
    plt.figure(figsize=(10,6))

    sorted_samples = sorted(samples)
    emp_cdf = empirical_cdf(sorted_samples)

    # CDF empírica
    plt.step(sorted_samples, emp_cdf, where="post", label="Empirical CDF")

    # CDF teórica
    x = np.linspace(0, max(samples), 1000)
    y = [gamma_cdf(val, alpha, beta) for val in x]

    plt.plot(x, y, 'r', label="Theoretical CDF")

    plt.title(f"CDF Comparison (α={alpha}, β={beta})")
    plt.legend()
    plt.show()