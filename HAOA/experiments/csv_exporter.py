import csv
import os

class CSVExporter:

```
def __init__(self):

    self.base_path = "csv_results"

    os.makedirs(
        self.base_path,
        exist_ok=True
    )

# -----------------------------------------
# Save benchmark summary
# -----------------------------------------

def export_summary(
    self,
    all_results
):

    file_path = \
        os.path.join(
            self.base_path,
            "summary_results.csv"
        )

    with open(
        file_path,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([

            "Benchmark",
            "Best Score",
            "Execution Time"

        ])

        # Rows
        for result in all_results:

            writer.writerow([

                result["benchmark"],

                result["best_score"],

                result["execution_time"]

            ])

    print(
        f"\nCSV summary saved: "
        f"{file_path}"
    )

# -----------------------------------------
# Save convergence curves
# -----------------------------------------

def export_convergence(
    self,
    all_results
):

    file_path = \
        os.path.join(
            self.base_path,
            "convergence_curves.csv"
        )

    with open(
        file_path,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([

            "Benchmark",
            "Iteration",
            "Best Score"

        ])

        # Curves
        for result in all_results:

            benchmark = \
                result["benchmark"]

            curve = \
                result["convergence_curve"]

            for iteration, score in \
                    enumerate(curve):

                writer.writerow([

                    benchmark,

                    iteration + 1,

                    score
                ])

    print(
        f"Convergence CSV saved: "
        f"{file_path}"
    )
```
