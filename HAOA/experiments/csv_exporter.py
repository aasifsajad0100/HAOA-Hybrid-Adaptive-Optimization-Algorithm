import csv
import os


class CSVExporter:

    def __init__(self):

        self.output_directory = "results/csv"

        os.makedirs(self.output_directory, exist_ok=True)

    def export_summary(self, all_results):

        file_path = os.path.join(
            self.output_directory,
            "summary.csv"
        )

        with open(file_path, "w", newline="") as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow([
                "Benchmark",
                "Best Score",
                "Execution Time"
            ])

            for result in all_results:

                writer.writerow([
                    result["benchmark"],
                    result["best_score"],
                    result["execution_time"]
                ])

        print(f"Saved: {file_path}")

    def export_convergence(self, all_results):

        file_path = os.path.join(
            self.output_directory,
            "convergence.csv"
        )

        with open(file_path, "w", newline="") as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow([
                "Benchmark",
                "Iteration",
                "Best Score"
            ])

            for result in all_results:

                benchmark_name = result["benchmark"]

                convergence_curve = result["convergence_curve"]

                for iteration, score in enumerate(convergence_curve):

                    writer.writerow([
                        benchmark_name,
                        iteration + 1,
                        score
                    ])

        print(f"Saved: {file_path}")
