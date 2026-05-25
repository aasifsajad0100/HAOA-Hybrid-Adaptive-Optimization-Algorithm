from benchmark_functions.sphere import sphere
from benchmark_functions.rastrigin import rastrigin
from benchmark_functions.rosenbrock import rosenbrock
from benchmark_functions.ackley import ackley
from benchmark_functions.griewank import griewank


class BenchmarkManager:

    def __init__(self):

        self.benchmarks = {

            "Sphere": {
                "function": sphere,
                "lower_bound": -100,
                "upper_bound": 100,
                "global_optimum": 0,
                "type": "Unimodal"
            },

            "Rastrigin": {
                "function": rastrigin,
                "lower_bound": -5.12,
                "upper_bound": 5.12,
                "global_optimum": 0,
                "type": "Multimodal"
            },

            "Rosenbrock": {
                "function": rosenbrock,
                "lower_bound": -30,
                "upper_bound": 30,
                "global_optimum": 0,
                "type": "Valley-Shaped"
            },

            "Ackley": {
                "function": ackley,
                "lower_bound": -32,
                "upper_bound": 32,
                "global_optimum": 0,
                "type": "Multimodal"
            },

            "Griewank": {
                "function": griewank,
                "lower_bound": -600,
                "upper_bound": 600,
                "global_optimum": 0,
                "type": "Multimodal"
            }
        }

    def get_all_benchmarks(self):
        return self.benchmarks

    def get_benchmark(self, name):
        return self.benchmarks[name]