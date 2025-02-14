class Car:
    def __init__(c, brand, model, year):
        c.brand = brand
        c.model = model
        c.year = year

    def display_info(c):
        print(f"Car Brand: {c.brand}")
        print(f"Car Model: {c.model}")
        print(f"Year: {c.year}")
        

car1 = Car("Ford", "F-Series", 2018)
print("\nCar 1 Details:")
car1.display_info()

car2 = Car("Honda", "CR-V", 2020)
print("\nCar 2 Details:")
car2.display_info()
