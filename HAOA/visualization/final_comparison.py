import pandas as pd
import matplotlib.pyplot as plt


def generate_final_comparison():

    algorithms = [
        "HAOA",
        "PSO"
    ]

    scores = [
        14.646,
        23.972
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        algorithms,
        scores,
        label="Optimization Score"
    )

    plt.xlabel("Algorithms")

    plt.ylabel("Final Score")

    plt.title(
        "HAOA vs PSO Comparison"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/figures/final_comparison.png"
    )

    print(
        "Saved: results/figures/final_comparison.png"
    )


if __name__ == "__main__":

    generate_final_comparison()
