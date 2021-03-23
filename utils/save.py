from typing import List, Dict

import pandas as pd


def save_to_excel(data: List[Dict], file_name: str):
    df = pd.DataFrame(data)
    df.to_excel(f"out/{file_name}")
