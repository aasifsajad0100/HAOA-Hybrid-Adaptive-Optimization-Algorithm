import numpy as np


def generate_dataset():

    np.random.seed(42)

    dataset = np.random.uniform(
        -10,
        10,
        (
            100,
            10
        )
    )

    np.savetxt(
        "results/datasets/sample_dataset.csv",
        dataset,
        delimiter=","
    )

    print(
        "Dataset saved:"
        " results/datasets/sample_dataset.csv"
    )

    return dataset