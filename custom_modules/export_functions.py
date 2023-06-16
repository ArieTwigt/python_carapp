import pandas as pd
import os
from datetime import datetime


def export_to_csv(df: pd.DataFrame, brand:str) -> None:
    # create the folder for the car export
    export_folder = f"export/{brand}" 

    # create the sub-directory
    os.makedirs(export_folder, exist_ok=True)

    # create a string containing the date and time
    current_date_time = datetime.now()
    current_date_time_str = current_date_time.strftime("%Y%m%d_%H%M%S")

    # create the export folder
    export_filename = f"{export_folder}/{brand}_{current_date_time_str}.csv"

    print(f"Exporting to: {export_filename}")

    # export to csv
    df.to_csv(export_filename, sep=";", index=False)

    print(f"✅ Successfully exported to {export_filename}")