from typing import Callable

import pandas as pd


path_to_data = "data/data.csv"
try:
    df = pd.read_csv(path_to_data)
except FileNotFoundError:
    columns = ["id", "username", "input_tokens", "output_tokens", "success", "messages"]
    df = pd.DataFrame(columns=columns)


def log_data(func: Callable):
    def wrapper(*args, **kwargs):
        messages, usages = func(*args, **kwargs)
        
        try:
            id = df.iloc[-1]["id"] + 1
        except IndexError:
            id = 0
        
        username = kwargs["user"].name

        input_tokens_total = sum([usage.prompt_tokens for usage in usages])
        output_tokens_total = sum([usage.completion_tokens for usage in usages])

        success = messages[-1]["content"] == "DONE"

        data = {
            "id": id, 
            "username": username, 
            "input_tokens": input_tokens_total, 
            "output_tokens": output_tokens_total, 
            "success": success, 
            "messages": messages
        }

        df.loc[df.shape[0]] = data # type: ignore

        df.to_csv(path_to_data)

        return messages, usages
    return wrapper
