from custom_modules.import_functions import import_cars_brand
from custom_modules.conversion_functions import cars_list_to_df
from custom_modules.export_functions import export_to_csv

# specify the brand
selected_brand = input("Insert a brand:\n")

# import the cars
cars_list = import_cars_brand(selected_brand)

# conver the cars to a DataFrame
cars_df = cars_list_to_df(cars_list)

# export the data frame
export_to_csv(cars_df, selected_brand)