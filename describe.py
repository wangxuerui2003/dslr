import numpy as np
import pandas as pd
import sys
import math


TARGET_COLUMN = "Hogwarts House"
NUMERICAL_FEATURE_COLUMNS = [
    "Arithmancy",
    "Astronomy",
    "Herbology",
    "Defense Against the Dark Arts",
    "Divination",
    "Muggle Studies",
    "Ancient Runes",
    "History of Magic",
    "Transfiguration",
    "Potions",
    "Care of Magical Creatures",
    "Charms",
    "Flying",
]

STATISTICS = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]


def get_percentile(sorted: np.ndarray, percent: float, count: int):
    pos = (count - 1) * percent
    lower_index = int(np.floor(pos))
    upper_index = int(np.ceil(pos))
    return sorted[lower_index] + (sorted[upper_index] - sorted[lower_index]) * (
        pos - lower_index
    )


def get_statistics(column: np.ndarray):
    column = column[~np.isnan(column)]

    count = 0
    sum = 0
    min_row = float("inf")
    max_row = float("-inf")

    for row in column:
        count += 1
        sum += row
        min_row = min(min_row, row)
        max_row = max(max_row, row)

    # mean
    mean = sum / count

    # std
    squared_diff_sum = 0
    for row in column:
        squared_diff_sum += (row - mean) ** 2
    var = squared_diff_sum / (count - 1)
    std = math.sqrt(var)

    sorted_col = np.sort(column)

    # 25%
    p25 = get_percentile(sorted_col, 0.25, count)
    # 50%
    p50 = get_percentile(sorted_col, 0.50, count)
    # 75%
    p75 = get_percentile(sorted_col, 0.75, count)

    return (count, mean, std, min_row, p25, p50, p75, max_row)


def main(dataset_filename: str):
    try:
        df = pd.read_csv(dataset_filename)
    except FileNotFoundError as e:
        print(f"{dataset_filename} not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Invalid csv file: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        numerical_features = df[NUMERICAL_FEATURE_COLUMNS]
        statistics_df = pd.DataFrame(columns=NUMERICAL_FEATURE_COLUMNS, index=STATISTICS)

        for col_name, col_data in numerical_features.items():
            statistics_df[col_name] = get_statistics(col_data.to_numpy())

        print(statistics_df)
    except Exception as e:
        print(f"Invalid dataset: {e}.", file=sys.stderr)
        sys.exit(1)

    # For reference
    # print(numerical_features.describe())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <dataset.csv>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
