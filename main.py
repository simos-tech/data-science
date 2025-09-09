import numpy as np
import pandas as pd

def read_data(data_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_path, delimiter=';')
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: {data_path} not found.")
        return None
    
def stats(feature: pd.Series, method: str) -> float:
    method = method.lower().strip()
    if method == 'mean':
        return feature.mean()
    elif method == 'std':
        return feature.std()
    elif method == 'describe' or method == '':
        return feature.describe()
    else:
        raise ValueError(f"Method '{method}' not supported. Use 'mean', 'std', or 'describe'.")

if __name__ == '__main__':

    df = read_data("data/car.csv")

    print(stats(df["Speed"], 'mean'))
    
