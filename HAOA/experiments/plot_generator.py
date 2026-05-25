import os
import matplotlib.pyplot as plt


class PlotGenerator:

    def __init__(self):

        self.output_directory = "results/figures"

        os.makedirs(self.output_directory, exist_ok=True)

    def generate_convergence_plot(self, all_results):

        plt.figure(figsize=(10, 6))

        for result in all_results:

            plt.plot(
                result["convergence_curve"],
                label=result["benchmark"]
            )

        plt.xlabel("Iteration")

        plt.ylabel("Best Score")

        plt.title("HAOA Convergence Curves")

        plt.legend()

        plt.grid(True)

        file_path = os.path.join(
            self.output_directory,
            "convergence_plot.png"
        )

        plt.savefig(file_path)

        plt.close()

        print(f"Saved: {file_path}")

    def generate_score_plot(self, all_results):

        benchmark_names = []
        benchmark_scores = []

        for result in all_results:

            benchmark_names.append(
                result["benchmark"]
            )

            benchmark_scores.append(
                result["best_score"]
            )

        plt.figure(figsize=(10, 6))

        plt.bar(
            benchmark_names,
            benchmark_scores
        )

        plt.xlabel("Benchmark")

        plt.ylabel("Best Score")

        plt.title("HAOA Benchmark Performance")

        plt.grid(True)

        file_path = os.path.join(
            self.output_directory,
            "score_plot.png"
        )

        plt.savefig(file_path)

        plt.close()

        print(f"Saved: {file_path}")
