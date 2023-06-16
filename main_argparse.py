from custom_modules.import_functions import import_cars_brand
from custom_modules.conversion_functions import cars_list_to_df
from custom_modules.export_functions import export_to_csv

import argparse

# initate the argument parser
parser = argparse.ArgumentParser()

# add arguments to the argument parser
parser.add_argument("--brand", "-b", 
                    required=True,
                    type=str,
                    help="Specify a brand to import")

parser.add_argument("--export", 
                    type=str,
                    required=False,
                    choices=['print', 'csv'],
                    default='print',
                    help="Specify the way to export the data (default is 'print')")

## parse the arguments
args = parser.parse_args()


# get the brand from the arguments
selected_brand = args.brand # bvb. "audi"
export = args.export

# use the functions


# import the cars from the api
cars_list = import_cars_brand(selected_brand)

# convert the cars list to a data frame
cars_df = cars_list_to_df(cars_list)

# export the data frame
if export == 'csv':
    print("Exporting")
    export_to_csv(cars_df, selected_brand)
else:
    print(cars_df)
