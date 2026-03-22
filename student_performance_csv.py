import pandas as pd

def load_data():
    return pd.read_csv("student_data.csv")

def process_data(df):
    df["average"] = (df["math"] + df["science"] + df["english"]) / 3
    return df

def top_student(df):
    return df.sort_values("average", ascending=False).iloc[0]
