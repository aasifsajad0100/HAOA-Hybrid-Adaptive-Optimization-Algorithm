import numpy as np
import math


class HAOA:

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

        self.best_solution = None

        self.best_score = float("inf")

        self.convergence_curve = []

        self.stagnation_counter = 0

    def evaluate_population(self):

        improved = False

        for individual in self.population:

            fitness = (
                self.objective_function(
                    individual
                )
            )

            if fitness < self.best_score:

                self.best_score = fitness

                self.best_solution = (
                    individual.copy()
                )

                improved = True

        if improved:

            self.stagnation_counter = 0

        else:

            self.stagnation_counter += 1

    def levy_flight(self):

        beta = 1.5

        sigma = (
            (
                math.gamma(1 + beta)
                * np.sin(np.pi * beta / 2)
            )
            /
            (
                math.gamma(
                    (1 + beta) / 2
                )
                * beta
                * 2 ** (
                    (beta - 1) / 2
                )
            )
        ) ** (1 / beta)

        u = np.random.randn(
            self.dimension
        ) * sigma

        v = np.random.randn(
            self.dimension
        )

        step = (
            u
            / (
                np.abs(v) ** (
                    1 / beta
                )
                + 1e-10
            )
        )

        return step

    def update_population(
        self,
        iteration
    ):

        progress = (
            iteration
            / self.max_iterations
        )

        inertia_weight = (
            0.95
            - 0.6 * progress
        )

        adaptive_learning = (
            1.8
            * (1 - progress)
        )

        mutation_strength = (
            0.003
            * (1 - progress)
        )

        elite = (
            self.best_solution.copy()
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

            r3 = np.random.rand(
                self.dimension
            )

            direction = (
                elite
                - self.population[i]
            )

            exploration = (

                adaptive_learning
                * r2
                * (
                    np.random.uniform(
                        self.lower_bound,
                        self.upper_bound,
                        self.dimension
                    )
                    - self.population[i]
                )
            )

            exploitation = (

                1.4
                * adaptive_learning
                * r1
                * direction
            )

            elite_refinement = (

                0.15
                * r3
                * (
                    elite
                    - self.population[i]
                )
            )

            self.velocity[i] = (

                inertia_weight
                * self.velocity[i]

                + exploitation

                + 0.15 * exploration

                + elite_refinement
            )

            velocity_limit = (
                0.2
                * (
                    self.upper_bound
                    - self.lower_bound
                )
            )

            self.velocity[i] = np.clip(
                self.velocity[i],
                -velocity_limit,
                velocity_limit
            )

            mutation = (

                mutation_strength
                * np.random.randn(
                    self.dimension
                )
            )

            new_position = (

                self.population[i]

                + self.velocity[i]

                + mutation
            )

            if self.stagnation_counter > 25:

                levy_jump = (
                    0.005
                    * self.levy_flight()
                )

                new_position += levy_jump

            if progress > 0.75:

                local_refinement = (

                    0.03
                    * (
                        elite
                        - new_position
                    )
                )

                new_position += (
                    local_refinement
                )

            new_position = np.clip(
                new_position,
                self.lower_bound,
                self.upper_bound
            )

            current_fitness = (
                self.objective_function(
                    self.population[i]
                )
            )

            new_fitness = (
                self.objective_function(
                    new_position
                )
            )

            if new_fitness < current_fitness:

                self.population[i] = (
                    new_position
                )

    def optimize(self):

        print("\nRunning HAOA...\n")

        for iteration in range(
            self.max_iterations
        ):

            self.evaluate_population()

            self.update_population(
                iteration
            )

            self.convergence_curve.append(
                self.best_score
            )

            print(
                f"Iteration "
                f"{iteration + 1}/"
                f"{self.max_iterations}"
                f" | Best Score: "
                f"{self.best_score:.10e}"
            )

        return {

            "best_score":
                self.best_score,

            "best_solution":
                self.best_solution,

            "convergence_curve":
                self.convergence_curve
        }