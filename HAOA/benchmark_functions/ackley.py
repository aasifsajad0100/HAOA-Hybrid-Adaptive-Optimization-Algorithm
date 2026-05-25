import numpy as np


def ackley(x):

    n = len(x)

    term1 = (

        -20
        * np.exp(
            -0.2
            * np.sqrt(
                np.sum(x ** 2) / n
            )
        )
    )

    term2 = (

        -np.exp(
            np.sum(
                np.cos(
                    2 * np.pi * x
                )
            ) / n
        )
    )

    return (
        term1
        + term2
        + 20
        + np.e
    )
