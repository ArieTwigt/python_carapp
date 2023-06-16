import pandas as pd
import numpy as np


def cars_list_to_df(cars_list: list) -> pd.DataFrame:
    """
    Function to convert a list of cars to a pandas DataFrame

    Params:
    * cars_list (list of cars)

    Returns:
    * cars_df (DataFrame of cars)

    """

    # create the DataFrame from the list
    cars_df = pd.DataFrame(cars_list)

    # 1. selecteer subset aan kolommen
    # cars_df.columns (zie beschikbare kolommen)
    selected_columns = ['kenteken', 'voertuigsoort', 
                        'merk', 'catalogusprijs', 
                        'eerste_kleur']
    
    cars_df_subset = cars_df[selected_columns]

    # 2. converteer naar juiste data typen
    # cars_df_subset.info() (informatie over de kolommen)
    # Convert 'catalogusprijs' to float
    cars_df_subset['catalogusprijs'] = cars_df_subset['catalogusprijs'].astype(float)

    # 3. wegfilteren ongewenste waarden (a. lege waarden), (b. te lage of te hoge waarden)

    # replace the NaN values for 0
    cars_df_subset['catalogusprijs'] = cars_df_subset['catalogusprijs'].fillna(0)

    # filter the DataFrame for cars with catalogusprijs higher than 0
    cars_df_subset =  cars_df_subset.query("catalogusprijs > 0 & voertuigsoort == 'Personenauto'")

    # add an additional column 
    cars_df_subset['prijscategorie'] = np.where(cars_df_subset['catalogusprijs'] < 20000, "normaal", "hoog")
                                     # np.where(de conditie, als conditie waar is, als conditie niet waar is)
    
    return cars_df_subset