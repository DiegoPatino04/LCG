from config.parameters import *
from simulation.gamma_pipeline import GammaSimulation
from analysis.plotting import plot_histogram_with_pdf, plot_cdf_comparison


def main():

    simulation = GammaSimulation(
        ALPHA,
        BETA,
        SEED,
        LCG_A,
        LCG_C,
        LCG_M
    )

    print(f"\nGenerating {SAMPLE_SIZE} Gamma samples (α={ALPHA}, β={BETA})...\n")

    # ===== MODO DEBUG (muestra trazabilidad) =====
    if PRINT_TRACE:
        results = simulation.generate_samples_with_trace(SAMPLE_SIZE)

        print(f"{'i':<5}{'Xi':<30}{'Ri':<30}{'Ni'}")
        print("-" * 100)

        for row in results[:MAX_PRINT_ROWS]:
            print(f"{row['i']:<5}{str(row['Xi']):<30}{str(row['Ri']):<30}{round(row['Ni'],6)}")

        samples = [row["Ni"] for row in results]

    # ===== MODO PERFORMANCE =====
    else:
        samples = simulation.generate_samples(SAMPLE_SIZE)

    print("\nGenerating plots...\n")

    plot_histogram_with_pdf(samples, ALPHA, BETA, BINS)
    plot_cdf_comparison(samples, ALPHA, BETA)

    print("Done.")


if __name__ == "__main__":
    main()