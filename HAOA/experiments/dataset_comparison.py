import time
import csv
import numpy as np
import matplotlib.pyplot as plt

from HAOA.algorithm.haoa import HAOA

from HAOA.benchmark_functions.rastrigin import rastrigin
from HAOA.benchmark_functions.ackley import ackley
from HAOA.benchmark_functions.griewank import griewank
from HAOA.benchmark_functions.rosenbrock import rosenbrock


class SimplePSO:

    def __init__(
        self,
        objective_function,
        dimension,
        lower_bound,
        upper_bound,
        population_size,
        max_iterations
    ):

        self.objective_function = (
            objective_function
        )

        self.dimension = dimension

        self.lower_bound = lower_bound

        self.upper_bound = upper_bound

        self.population_size = (
            population_size
        )

        self.max_iterations = (
            max_iterations
        )

        self.population = np.random.uniform(
            self.lower_bound,
            self.upper_bound,
            (
                self.population_size,
                self.dimension
            )
        )

        self.velocity = np.zeros(
            (
                self.population_size,
                self.dimension
            )
        )

        self.personal_best_positions = (
            self.population.copy()
        )

        self.personal_best_scores = np.full(
            self.population_size,
            np.inf
        )

        self.global_best_position = None

        self.global_best_score = np.inf

        self.convergence_curve = []

    def optimize(self):

        w = 0.7
        c1 = 1.5
        c2 = 1.5

        print("\nRunning PSO...\n")

        for iteration in range(
            self.max_iterations
        ):

            for i in range(
                self.population_size
            ):

                fitness = (
                    self.objective_function(
                        self.population[i]
                    )
                )

                if (
                    fitness
                    < self.personal_best_scores[i]
                ):

                    self.personal_best_scores[i] = (
                        fitness
                    )

                    self.personal_best_positions[i] = (
                        self.population[i].copy()
                    )

                if (
                    fitness
                    < self.global_best_score
                ):

                    self.global_best_score = (
                        fitness
                    )

                    self.global_best_position = (
                        self.population[i].copy()
                    )

            for i in range(
                self.population_size
            ):

                r1 = np.random.rand(
                    self.dimension
                )

                r2 = np.random.rand(
                    self.dimension
                )

                cognitive = (

                    c1
                    * r1
                    * (
                        self.personal_best_positions[i]
                        - self.population[i]
                    )
                )

                social = (

                    c2
                    * r2
                    * (
                        self.global_best_position
                        - self.population[i]
                    )
                )

                self.velocity[i] = (

                    w
                    * self.velocity[i]

                    + cognitive

                    + social
                )

                self.population[i] += (
                    self.velocity[i]
                )

                self.population[i] = np.clip(
                    self.population[i],
                    self.lower_bound,
                    self.upper_bound
                )

            self.convergence_curve.append(
                self.global_best_score
            )

            print(
                f"PSO Iteration "
                f"{iteration + 1}/"
                f"{self.max_iterations}"
                f" | Best Score: "
                f"{self.global_best_score:.10e}"
            )

        return {

            "best_score":
                self.global_best_score,

            "convergence_curve":
                self.convergence_curve
        }


benchmarks = {

    "Rastrigin": rastrigin,

    "Ackley": ackley,

    "Griewank": griewank,

    "Rosenbrock": rosenbrock
}


def run_dataset_test():

    print("=" * 60)
    print(" HAOA BENCHMARK COMPARISON TEST ")
    print("=" * 60)

    dimension = 30

    lower_bound = -30

    upper_bound = 30

    population_size = 50

    max_iterations = 200

    results = []

    for benchmark_name, objective_function in benchmarks.items():

        print("\n" + "=" * 60)
        print(f"Benchmark: {benchmark_name}")
        print("=" * 60)

        haoa_start = time.time()

        haoa = HAOA(
            objective_function,
            dimension,
            lower_bound,
            upper_bound,
            population_size,
            max_iterations
        )

        haoa_result = haoa.optimize()

        haoa_time = (
            time.time()
            - haoa_start
        )

        pso_start = time.time()

        pso = SimplePSO(
            objective_function,
            dimension,
            lower_bound,
            upper_bound,
            population_size,
            max_iterations
        )

        pso_result = pso.optimize()

        pso_time = (
            time.time()
            - pso_start
        )

        print(
            f"\nHAOA Best Score : "
            f"{haoa_result['best_score']:.10e}"
        )

        print(
            f"PSO Best Score  : "
            f"{pso_result['best_score']:.10e}"
        )

        results.append({

            "Benchmark":
                benchmark_name,

            "HAOA Score":
                haoa_result["best_score"],

            "PSO Score":
                pso_result["best_score"],

            "HAOA Time":
                haoa_time,

            "PSO Time":
                pso_time
        })

        plt.figure(figsize=(10, 6))

        plt.plot(
            haoa_result[
                "convergence_curve"
            ],
            label="HAOA"
        )

        plt.plot(
            pso_result[
                "convergence_curve"
            ],
            label="PSO"
        )

        plt.xlabel("Iteration")

        plt.ylabel("Fitness")

        plt.title(
            f"{benchmark_name} Convergence"
        )

        plt.legend()

        plt.grid(True)

        plt.savefig(

            f"HAOA/results/"
            f"{benchmark_name}_comparison.png"
        )

        plt.close()

        print(
            f"Saved Plot: "
            f"HAOA/results/"
            f"{benchmark_name}_comparison.png"
        )

    csv_file = (
        "HAOA/results/"
        "benchmark_comparison.csv"
    )

    with open(
        csv_file,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            "Benchmark",
            "HAOA Score",
            "PSO Score",
            "HAOA Time",
            "PSO Time"
        ])

        for row in results:

            writer.writerow([

                row["Benchmark"],
                row["HAOA Score"],
                row["PSO Score"],
                row["HAOA Time"],
                row["PSO Time"]
            ])

    print("\n" + "=" * 60)
    print(" FINAL COMPARISON RESULTS ")
    print("=" * 60)

    for row in results:

        print("\n" + "-" * 50)

        print(
            f"Benchmark : "
            f"{row['Benchmark']}"
        )

        print(
            f"HAOA Score: "
            f"{row['HAOA Score']:.10e}"
        )

        print(
            f"PSO Score : "
            f"{row['PSO Score']:.10e}"
        )

        if (
            row["HAOA Score"]
            < row["PSO Score"]
        ):

            print(
                "Winner    : HAOA"
            )

        else:

            print(
                "Winner    : PSO"
            )

    print("\nCSV saved:")
    print(csv_file)


if __name__ == "__main__":

    run_dataset_test()
