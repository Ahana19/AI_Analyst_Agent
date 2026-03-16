import pandas as pd

def analyze(df: pd.DataFrame) -> dict:
    numeric_df = df.select_dtypes(include="number")
    return {
        "summary": df.describe().to_dict(),
        "correlations": numeric_df.corr().to_dict(),
        "top_columns": list(df.columns),
        "row_count": len(df),
        "column_count": len(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict()
    }
