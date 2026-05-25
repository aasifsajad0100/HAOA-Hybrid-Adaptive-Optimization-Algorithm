import pandas as pd
import matplotlib.pyplot as plt


def generate_comparison_plot():

    data = pd.read_csv(
        "results/csv/summary.csv"
    )

    benchmarks = data["benchmark"]

    scores = data["best_score"]

    plt.figure(figsize=(10, 6))

    plt.bar(
        benchmarks,
        scores,
        label="HAOA Scores"
    )

    plt.xlabel("Benchmarks")

    plt.ylabel("Best Score")

    plt.title(
        "HAOA Benchmark Comparison"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/figures/benchmark_comparison.png"
    )

    print(
        "Saved: results/figures/benchmark_comparison.png"
    )


def generate_dataset_vs_pso():

    algorithms = [
        "HAOA",
        "PSO"
    ]

    scores = [
        14.64,
        23.97
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        algorithms,
        scores,
        label="Final Error"
    )

    plt.xlabel("Algorithms")

    plt.ylabel("Final Score")

    plt.title(
        "HAOA vs PSO Dataset Optimization"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/figures/haoa_vs_pso.png"
    )

    print(
        "Saved: results/figures/haoa_vs_pso.png"
    )


if __name__ == "__main__":

    generate_comparison_plot()

    generate_dataset_vs_pso()
