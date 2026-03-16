import pandas as pd

def clean_data(df: pd.DataFrame) -> dict:
    report = {}
    report["original_shape"] = df.shape

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Fill or drop nulls
    null_counts = df.isnull().sum()
    report["nulls_found"] = null_counts[null_counts > 0].to_dict()
    df = df.fillna(df.median(numeric_only=True))
    df = df.fillna("Unknown")

    # Fix data types
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    report["cleaned_shape"] = df.shape
    return {"df": df, "report": report}