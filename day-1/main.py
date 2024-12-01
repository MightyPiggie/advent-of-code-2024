import numpy as np
import pandas as pd

def main():
    total = 0
    data = pd.read_csv("input.txt", dtype=int, sep='   ', header=None)

    column_1 = data[0].to_numpy()
    column_2 = data[1].to_numpy()
    for _ in range(0, len(data)):
        column_1_min = np.min(column_1)
        column_2_min = np.min(column_2)
        column_1 = np.delete(column_1, np.where(column_1 == column_1_min)[0][0])
        column_2 = np.delete(column_2, np.where(column_2 == column_2_min)[0][0])
        total += abs(column_1_min - column_2_min)
    print("First Awnser: ", total)

    total_2 = 0
    data = pd.read_csv("input.txt", dtype=int, sep='   ', header=None)

    column_1 = data[0].to_numpy()
    column_2 = data[1].to_numpy()

    for item in column_1:
        count = np.count_nonzero(column_2 == item)
        total_2 += count*item
    
    print("Second Awnser: ", total_2)
main()
    