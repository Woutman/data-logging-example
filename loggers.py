from typing import Callable

import pandas as pd


path_to_data = "data.csv"
try:
    df = pd.read_csv(path_to_data)
except FileNotFoundError:
    columns = ["id", "username", "input_tokens", "output_tokens", "success", "messages"]
    df = pd.DataFrame()


def log_data(func: Callable):
    def wrapper(*args, **kwargs):
        messages, usages = func(*args, **kwargs)

