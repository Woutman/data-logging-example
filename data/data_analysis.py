import ast

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme()

COST_INPUT_TOKENS_DOLLARS = 2.5 / 1_000_000
COST_OUTPUT_TOKENS_DOLLARS = 10 / 1_000_000

path_to_data = "data.csv"
df = pd.read_csv(path_to_data, index_col=0)


def prep_data(df: pd.DataFrame) -> pd.DataFrame:
    df['cost_dollars'] = COST_INPUT_TOKENS_DOLLARS * df['input_tokens'] + COST_OUTPUT_TOKENS_DOLLARS * df['output_tokens']
    df['num_messages'] = df['messages'].apply(lambda x: len(ast.literal_eval(x)))
    return df


def plot_cost_per_user(df: pd.DataFrame) -> None:
    cost_per_user = df.groupby('username', as_index=False)['cost_dollars'].sum()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=cost_per_user, x='username', y='cost_dollars') # type: ignore
    plt.title('Total Cost per User')
    plt.xlabel('Username')
    plt.ylabel('Cost in Dollars')
    plt.xticks(rotation=45)
    plt.show()


def plot_avg_cost_per_success(df: pd.DataFrame) -> None:
    avg_cost_per_success = df.groupby('success', as_index=False)['cost_dollars'].mean()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=avg_cost_per_success, x='success', y='cost_dollars') # type: ignore
    plt.title('Average Cost per Success and Failure')
    plt.xlabel('Success')
    plt.ylabel('Cost in Dollars')
    plt.xticks(rotation=45)
    plt.show()


def plot_ratio_of_successes_per_user(df: pd.DataFrame) -> None:
    ratio_of_successes_per_user = df.groupby('username', as_index=False)['success'].mean()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=ratio_of_successes_per_user, x='username', y='success') # type: ignore
    plt.title('Ratio of Successes to Failures per User')
    plt.xlabel('Username')
    plt.ylabel('Ratio of Successes to Failures')
    plt.xticks(rotation=45)
    plt.show()


def plot_avg_num_messages_per_user(df: pd.DataFrame) -> None:
    avg_num_messages = df.groupby('username', as_index=False)['num_messages'].mean()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=avg_num_messages, x='username', y='num_messages') # type: ignore
    plt.title('Average Number of Messages per User')
    plt.xlabel('Username')
    plt.ylabel('Average Number of Messages')
    plt.xticks(rotation=45)
    plt.show()


def analyze_data():
    data = prep_data(df)
    plot_avg_num_messages_per_user(data)
    plot_avg_cost_per_success(data)
    plot_ratio_of_successes_per_user(data)
    plot_avg_num_messages_per_user(data)


if __name__ == "__main__":
    analyze_data()