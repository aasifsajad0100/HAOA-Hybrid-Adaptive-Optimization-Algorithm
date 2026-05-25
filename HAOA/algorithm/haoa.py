import random
import math

class HAOA:

```
def __init__(
    self,
    objective_function,
    dimension,
    lower_bound,
    upper_bound,
    population_size,
    max_iterations
):

    # Problem definition
    self.objective_function = objective_function
    self.dimension = dimension
    self.lower_bound = lower_bound
    self.upper_bound = upper_bound

    # Algorithm parameters
    self.population_size = population_size
    self.max_iterations = max_iterations

    # Initialize population
    self.population = [

        [
            random.uniform(
                lower_bound,
                upper_bound
            )

            for _ in range(dimension)
        ]

        for _ in range(population_size)
    ]

    # Evaluate fitness
    self.fitness = [

        objective_function(agent)

        for agent in self.population
    ]

    # Best solution
    self.best_index = self.fitness.index(
        min(self.fitness)
    )

    self.best_solution = \
        self.population[self.best_index]

    self.best_score = \
        self.fitness[self.best_index]

    # Convergence history
    self.convergence_curve = []

# -------------------------------------------------
# Main optimization process
# -------------------------------------------------

def optimize(self):

    for iteration in range(
        self.max_iterations
    ):

        # Adaptive switching probability
        adaptive_probability = \
            1 - (
                iteration /
                self.max_iterations
            )

        for i in range(
            self.population_size
        ):

            candidate = \
                self.population[i][:]

            # ---------------------------------
            # Exploration phase
            # ---------------------------------

            if random.random() < adaptive_probability:

                random_agent = random.randint(
                    0,
                    self.population_size - 1
                )

                for d in range(
                    self.dimension
                ):

                    r = random.random()

                    candidate[d] = \
                        self.best_solution[d] + \
                        r * (
                            self.population[i][d]
                            -
                            self.population[random_agent][d]
                        )

            # ---------------------------------
            # Exploitation phase
            # ---------------------------------

            else:

                alpha = random.random()

                for d in range(
                    self.dimension
                ):

                    candidate[d] = \
                        self.best_solution[d] + \
                        alpha * (
                            self.best_solution[d]
                            -
                            self.population[i][d]
                        )

            # Boundary control
            candidate = [

                max(
                    self.lower_bound,

                    min(
                        x,
                        self.upper_bound
                    )
                )

                for x in candidate
            ]

            # Evaluate candidate
            candidate_fitness = \
                self.objective_function(
                    candidate
                )

            # Greedy selection
            if candidate_fitness < self.fitness[i]:

                self.population[i] = candidate

                self.fitness[i] = \
                    candidate_fitness

            # Update global best
            if candidate_fitness < self.best_score:

                self.best_score = \
                    candidate_fitness

                self.best_solution = \
                    candidate[:]

        # Save convergence
        self.convergence_curve.append(
            self.best_score
        )

        # Progress display
        if (
            iteration % 50 == 0
            or
            iteration ==
            self.max_iterations - 1
        ):

            print(
                f"Iteration {iteration + 1} "
                f"| Best Score: "
                f"{self.best_score:.10f}"
            )

    return {
        "best_solution":
            self.best_solution,

        "best_score":
            self.best_score,

        "convergence_curve":
            self.convergence_curve
    }
