import pandas as pd
from . import constants


def export_csv(data, filename="data.csv"):
    data = pd.DataFrame(data, columns=constants.COLUMNS)
    data.to_csv(
        f"{constants.PATH}\{filename}",
        index=False,
    )
