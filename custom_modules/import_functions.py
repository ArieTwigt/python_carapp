import requests


def import_cars_brand(brand: str) -> list:
    """
    Function to import cars

    Params:
    * brand (brand of the car)

    Return:
    * list of cars
    """

    # uppercase the brand
    brand_upper = brand.upper()

    # create the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # send the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json() 

    # check if the data is empty
    if len(data) == 0:
        print("No data found")

    return data
