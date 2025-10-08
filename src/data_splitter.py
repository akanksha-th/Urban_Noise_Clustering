from sklearn.model_selection import train_test_split
import pandas as pd


def split_data(df, test_size=0.2, val_size=0.1, random_state=42):
    """Splits the data into training, validation, and test sets."""
    train_val_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    train_df, val_df = train_test_split(train_val_df, test_size=val_size/(1 - test_size), random_state=random_state)
    
    return train_df.reset_index(drop=True), val_df.reset_index(drop=True), test_df.reset_index(drop=True)