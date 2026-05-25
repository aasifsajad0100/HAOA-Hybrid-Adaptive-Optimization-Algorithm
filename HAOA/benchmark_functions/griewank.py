import numpy as np


def griewank(x):

    sum_term = np.sum(
        x ** 2
    ) / 4000

    prod_term = 1

    for i in range(len(x)):

        prod_term *= np.cos(
            x[i]
            / np.sqrt(i + 1)
        )

    return (
        sum_term
        - prod_term
        + 1
    )
