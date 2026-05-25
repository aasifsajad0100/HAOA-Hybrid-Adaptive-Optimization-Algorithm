import os
import matplotlib.pyplot as plt

class PlotGenerator:

```
def __init__(self):

    self.output_path = "graphs"

    os.makedirs(
        self.output_path,
        exist_ok=True
    )

# -------------------------------------------------
# Convergence plot
# -------------------------------------------------

def generate_convergence_plot(
    self,
    all_results
):

    plt.figure(figsize=(10, 6))

    for result in all_results:

        plt.plot(

            result["convergence_curve"],

            label=result["benchmark"]
        )

    plt.title(
        "HAOA Convergence Curves"
    )

    plt.xlabel("Iteration")

    plt.ylabel("Best Score")

    plt.legend()

    plt.grid(True)

    file_path = os.path.join(

        self.output_path,

        "convergence_plot.png"
    )

    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        f"Convergence plot saved: "
        f"{file_path}"
    )

# -------------------------------------------------
# Benchmark comparison bar chart
# -------------------------------------------------

def generate_score_plot(
    self,
    all_results
):

    benchmarks = [

        result["benchmark"]

        for result in all_results
    ]

    scores = [

        result["best_score"]

        for result in all_results
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(
        benchmarks,
        scores
    )

    plt.title(
        "HAOA Benchmark Performance"
    )

    plt.xlabel("Benchmark")

    plt.ylabel("Best Score")

    plt.grid(True)

    file_path = os.path.join(

        self.output_path,

        "benchmark_scores.png"
    )

    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        f"Score plot saved: "
        f"{file_path}"
    )
```
