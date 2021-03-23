from typing import List, Dict
import pandas as pd
import matplotlib.pyplot as plt


def create_bar(data: List[Dict], value_name: str, index_name: str):
    df = pd.DataFrame(data)
    plt.bar(df[index_name], df[value_name])
    plt.show()
