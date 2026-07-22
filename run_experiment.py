# Placeholder capstone script, swap in real analysis once decided.
import pandas as pd

DATA_PATH = "data/sample_dataset.csv"
N_ROWS = 5  # try changing this

df = pd.read_csv(DATA_PATH)
print(df.head(N_ROWS))
