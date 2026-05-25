import numpy as np


class PSO:

    def __init__(
        self,
        objective_function,
        dimension,
        lower_bound,
        upper_bound,
        population_size,
        max_iterations
    ):

        self.objective_function = objective_function

        self.dimension = dimension

        self.lower_bound = lower_bound

        self.upper_bound = upper_bound

        self.population_size = population_size

        self.max_iterations = max_iterations

        self.positions = np.random.uniform(
            lower_bound,
            upper_bound,
            (population_size, dimension)
        )

        self.velocities = np.random.uniform(
            -1,
            1,
            (population_size, dimension)
        )

        self.personal_best_positions = self.positions.copy()

        self.personal_best_scores = np.full(
            population_size,
            np.inf
        )

        self.global_best_position = None

        self.global_best_score = np.inf

        self.convergence_curve = []

    def optimize(self):

        w = 0.7
        c1 = 1.5
        c2 = 1.5

        for iteration in range(self.max_iterations):

            for i in range(self.population_size):

                fitness = self.objective_function(
                    self.positions[i]
                )

                if fitness < self.personal_best_scores[i]:

                    self.personal_best_scores[i] = fitness

                    self.personal_best_positions[i] = (
                        self.positions[i].copy()
                    )

                if fitness < self.global_best_score:

                    self.global_best_score = fitness

                    self.global_best_position = (
                        self.positions[i].copy()
                    )

            for i in range(self.population_size):

                r1 = np.random.rand(self.dimension)

                r2 = np.random.rand(self.dimension)

                cognitive = (
                    c1
                    * r1
                    * (
                        self.personal_best_positions[i]
                        - self.positions[i]
                    )
                )

                social = (
                    c2
                    * r2
                    * (
                        self.global_best_position
                        - self.positions[i]
                    )
                )

                self.velocities[i] = (
                    w * self.velocities[i]
                    + cognitive
                    + social
                )

                self.positions[i] += self.velocities[i]

                self.positions[i] = np.clip(
                    self.positions[i],
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
                f"{self.global_best_score:.10f}"
            )

        return {

            "best_score":
                self.global_best_score,

            "best_solution":
                self.global_best_position,

            "convergence_curve":
                self.convergence_curve
        }
