import time

from experiments.benchmark_manager import BenchmarkManager
from algorithm.haoa import HAOA

def run_all_experiments():

```
print("=" * 60)
print(" HAOA — Full Optimization Research Framework ")
print("=" * 60)

# Benchmark manager
benchmark_manager = BenchmarkManager()

benchmarks = \
    benchmark_manager.get_all_benchmarks()

# Common experiment settings
dimension = 10
population_size = 40
max_iterations = 300

# Store all results
all_results = []

# -------------------------------------------------
# Run all benchmark functions
# -------------------------------------------------

for benchmark_name, benchmark_data in \
        benchmarks.items():

    print("\n" + "─" * 50)
    print(f" Running Benchmark: {benchmark_name}")
    print("─" * 50)

    objective_function = \
        benchmark_data["function"]

    lower_bound = \
        benchmark_data["lower_bound"]

    upper_bound = \
        benchmark_data["upper_bound"]

    # Start timing
    start_time = time.time()

    # Initialize optimizer
    optimizer = HAOA(

        objective_function=objective_function,

        dimension=dimension,

        lower_bound=lower_bound,

        upper_bound=upper_bound,

        population_size=population_size,

        max_iterations=max_iterations
    )

    # Run optimization
    result = optimizer.optimize()

    # End timing
    end_time = time.time()

    execution_time = \
        end_time - start_time

    # Store results
    benchmark_result = {

        "benchmark":
            benchmark_name,

        "best_score":
            result["best_score"],

        "best_solution":
            result["best_solution"],

        "convergence_curve":
            result["convergence_curve"],

        "execution_time":
            execution_time
    }

    all_results.append(
        benchmark_result
    )

    # Display result
    print(
        f"\nBest Score: "
        f"{result['best_score']:.10f}"
    )

    print(
        f"Execution Time: "
        f"{execution_time:.4f} sec"
    )

print("\n" + "=" * 60)
print(" ALL BENCHMARKS COMPLETED ")
print("=" * 60)

return all_results
```

# -------------------------------------------------

# Main Execution

# -------------------------------------------------

if **name** == "**main**":

```
final_results = \
    run_all_experiments()
```
