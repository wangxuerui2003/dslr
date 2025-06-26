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

	fig, axes = plt.subplots(nrows=len(HOGWARTS_HOUSES), ncols=len(NUMERICAL_FEATURE_COLUMNS), figsize=(20, 6))

	# Add row labels (left side)
	for i, house in enumerate(HOGWARTS_HOUSES):
		axes[i, 0].set_ylabel(house, rotation=0, fontsize=12, ha='right', va='center')

	# Add column labels (top)
	for j, feature in enumerate(SHORTENED_NUMERICAL_FEATURE_COLUMNS):
		axes[0, j].set_title(feature, fontsize=12, pad=20)

	for i in range(len(HOGWARTS_HOUSES)):
		for j in range(len(NUMERICAL_FEATURE_COLUMNS)):
			data = df[df[TARGET_COLUMN] == HOGWARTS_HOUSES[i]][NUMERICAL_FEATURE_COLUMNS[j]].dropna().to_numpy()
			axes[i, j].hist(data, bins=30, color='skyblue')
			axes[i, j].tick_params(axis='both', labelsize=8)
	
	# Adjust layout to prevent overlap
	plt.tight_layout()
	plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <dataset.csv>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])

# Question: Which Hogwarts course has a homogeneous score distribution between all four houses?
# Answer: Care of Magical Creatures
		