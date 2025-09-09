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
    
def add_rnd_col(start: float, end: float, num: int) -> pd.Series:
    new_col = np.random.uniform(start, end, num)
    return new_col.astype(pd.Series)
    
def stats(feature: pd.Series, method: str) -> float:
    method = method.lower().strip()
    if method == 'mean':
        return np.mean(feature)
    elif method == 'std':
        return np.std(feature)
    elif method == 'describe' or method == '':
        return feature.describe()
    else:
        raise ValueError(f"Method '{method}' not supported. Use 'mean', 'std', or 'describe'.")

if __name__ == '__main__':

    df = read_data("data/car.csv")

    df['Rnd_Col'] = add_rnd_col(0.0, 10.0, len(df))

    print(df)
    
