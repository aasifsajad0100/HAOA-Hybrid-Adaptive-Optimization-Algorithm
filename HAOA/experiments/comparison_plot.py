import matplotlib.pyplot as plt
import os


class ComparisonPlot:

    def __init__(self):

        os.makedirs(
            "results/figures",
            exist_ok=True
        )

    def generate_comparison_plot(
        self,
        haoa_curve,
        pso_curve
    ):

        plt.figure(figsize=(10, 6))

        plt.plot(
            haoa_curve,
            label="HAOA",
            linewidth=2
        )

        plt.plot(
            pso_curve,
            label="PSO",
            linewidth=2
        )

        plt.xlabel("Iterations")

        plt.ylabel("Best Score")

        plt.title(
            "HAOA vs PSO Convergence"
        )

        plt.legend()

        plt.grid(True)

        path = (
            "results/figures/"
            "haoa_vs_pso.png"
        )

        plt.savefig(path)

        plt.close()

        print(f"Saved: {path}")
