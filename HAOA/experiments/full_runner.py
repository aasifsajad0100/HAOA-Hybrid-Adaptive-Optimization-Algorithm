import time

from HAOA.experiments.benchmark_manager import BenchmarkManager
from HAOA.experiments.csv_exporter import CSVExporter
from HAOA.experiments.plot_generator import PlotGenerator
from HAOA.algorithm.haoa import HAOA


def run_all_experiments():

    print("=" * 60)
    print("HAOA — Full Optimization Research Framework")
    print("=" * 60)

    benchmark_manager = BenchmarkManager()

    benchmarks = benchmark_manager.get_all_benchmarks()

    dimension = 10
    population_size = 40
    max_iterations = 300

    all_results = []

    for benchmark_name, benchmark_data in benchmarks.items():

        print("\n" + "─" * 50)
        print(f"Running Benchmark: {benchmark_name}")
        print("─" * 50)

        objective_function = benchmark_data["function"]
        lower_bound = benchmark_data["lower_bound"]
        upper_bound = benchmark_data["upper_bound"]

        start_time = time.time()

        optimizer = HAOA(
            objective_function=objective_function,
            dimension=dimension,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            population_size=population_size,
            max_iterations=max_iterations
        )

        result = optimizer.optimize()

        execution_time = time.time() - start_time

        benchmark_result = {
            "benchmark": benchmark_name,
            "best_score": result["best_score"],
            "best_solution": result["best_solution"],
            "convergence_curve": result["convergence_curve"],
            "execution_time": execution_time
        }

        all_results.append(benchmark_result)

        print(f"\nBest Score: {result['best_score']:.10f}")
        print(f"Execution Time: {execution_time:.4f} sec")

    csv_exporter = CSVExporter()

    csv_exporter.export_summary(all_results)
    csv_exporter.export_convergence(all_results)

    plot_generator = PlotGenerator()

    plot_generator.generate_convergence_plot(all_results)
    plot_generator.generate_score_plot(all_results)

    print("\n" + "=" * 60)
    print("ALL BENCHMARKS COMPLETED")
    print("=" * 60)

    return all_results


if __name__ == "__main__":

    final_results = run_all_experiments()
