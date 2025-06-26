import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

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
HOGWARTS_HOUSES = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]

SHORTENED_NUMERICAL_FEATURE_COLUMNS = [
    "Arith",
    "Astro",
    "Herbo",
    "Def Dark",
    "Divi",
    "MS",
    "AR",
    "HoM",
    "Trans",
    "Potions",
    "CoMC",
    "Charms",
    "Flying",
]

def read_data(filename: str) -> pd.DataFrame:
	try:
		df = pd.read_csv(filename)
		return df
	except FileExistsError:
		print(f"{filename} not found.", file=sys.stderr)
		sys.exit(1)
	except Exception as e:
		print(f"Invalid dataset file: {e}", file=sys.stderr)
		sys.exit(1)

def main(dataset_filename):
	df = read_data(dataset_filename)

	fig, axes = plt.subplots(nrows=len(NUMERICAL_FEATURE_COLUMNS), ncols=len(NUMERICAL_FEATURE_COLUMNS), figsize=(14, 12))

	# Add row labels (left side)
	for i, feature in enumerate(SHORTENED_NUMERICAL_FEATURE_COLUMNS):
		axes[i, 0].set_ylabel(feature, rotation=0, fontsize=12, ha='right', va='center')

	# Add column labels (top)
	for j, feature in enumerate(SHORTENED_NUMERICAL_FEATURE_COLUMNS):
		axes[0, j].set_title(feature, fontsize=12, pad=20)

	for i in range(len(NUMERICAL_FEATURE_COLUMNS)):
		for j in range(len(NUMERICAL_FEATURE_COLUMNS)):
			xy_data = df[[NUMERICAL_FEATURE_COLUMNS[i], NUMERICAL_FEATURE_COLUMNS[j]]].dropna()
			x = xy_data[NUMERICAL_FEATURE_COLUMNS[i]].to_numpy()
			y = xy_data[NUMERICAL_FEATURE_COLUMNS[j]].to_numpy()
			axes[i, j].scatter(x, y, s=0.2, color='skyblue')
			axes[i, j].tick_params(axis='both', labelsize=8)
			axes[i, j].set_yticks([])
			axes[i, j].set_xticks([])

	plt.grid(True)
	plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <dataset.csv>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])

# Question: What are the two features that are similar?
# Answer: Defense Against the Dark Arts and Astronomy, negatively linear relationship
		