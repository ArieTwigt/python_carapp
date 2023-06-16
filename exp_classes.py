class Car:

    purpose = "transport"
    availability = "available"


    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


    def reserve_car(self):
        self.availability = "reserved"
        print("Car is now reserved")


    def change_price(self, amount):
        print(f"Old price is {self.price}")
        
        # validate that the price cannot be lower than 0 
        if self.price + amount < 0:
            raise ValueError("The price cannot be lower than 0")
        
        self.price += amount
        print(f"New price is {self.price}")

    
    def export_text_file(self):

        # define the file name
        file_name = f"export/{self.brand}.txt"

        # define the file content
        file_content = f"{self.brand} - {self.model} - {self.price} - {self.availability}"

        # export the text file
        with open(file_name, "w") as file:
            file.write(file_content)

        print(f"📝 Wrote to text file {file_name}")

    
    def __repr__(self) -> str:
        return f"{self.brand} - {self.model} - {self.price} - ({self.availability})"


# initiate 2 car instances
my_car = Car("Audi", "A1", 10000)
my_car_2 = Car("BMW", "120", 12000)


# reserve the car
my_car.reserve_car()

pass