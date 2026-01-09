import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

def clean_and_encode(df):
    df_clean = df.copy()
    cat_cols = df_clean.select_dtypes('object').columns
    if len(cat_cols) > 0:
        oe = OrdinalEncoder()
        df_clean[cat_cols] = oe.fit_transform(df_clean[cat_cols])
    return df_clean

def scale_features(df, numeric_cols):
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df