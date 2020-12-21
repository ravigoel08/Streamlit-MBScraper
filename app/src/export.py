import pandas as pd
import base64
import streamlit as st


def export_csv(data, filename="data.csv"):
    if isinstance(data, pd.DataFrame):
        data = data.to_csv(index=False)
    b64 = base64.b64encode(data.encode()).decode()
    return f'<a href="data:file/text;base64,{b64}" download="{filename}">Click here to download CSV</a>'
