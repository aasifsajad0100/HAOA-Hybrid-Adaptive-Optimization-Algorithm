from HAOA.benchmark_functions.sphere import sphere
from HAOA.benchmark_functions.rastrigin import rastrigin
from HAOA.benchmark_functions.rosenbrock import rosenbrock
from HAOA.benchmark_functions.ackley import ackley
from HAOA.benchmark_functions.griewank import griewank


class BenchmarkManager:

    def __init__(self):

        self.benchmarks = {

            "Sphere": {
                "function": sphere,
                "lower_bound": -100,
                "upper_bound": 100
            },

            "Rastrigin": {
                "function": rastrigin,
                "lower_bound": -5.12,
                "upper_bound": 5.12
            },

            "Rosenbrock": {
                "function": rosenbrock,
                "lower_bound": -30,
                "upper_bound": 30
            },

            "Ackley": {
                "function": ackley,
                "lower_bound": -32,
                "upper_bound": 32
            },

            "Griewank": {
                "function": griewank,
                "lower_bound": -600,
                "upper_bound": 600
            }
        }

    def get_all_benchmarks(self):

        return self.benchmarks
