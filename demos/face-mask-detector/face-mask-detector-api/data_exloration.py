import pandas as pd

if __name__ == "__main__":

    csv_fp = "emily/val.csv"
    df = pd.read_csv(csv_fp)

    print(len(df))
