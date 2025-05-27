#Car Information System
Suppose we want to manage a list of cars, each with attributes like brand, model, and year, and perform operations such as sorting cars by year or filtering cars by brand.

Python Code :
CopyRun
# Data: List of cars
cars = [
    {"brand": "Toyota", "model": "Camry", "year": 2019},
    {"brand": "Honda", "model": "Accord", "year": 2018},
    {"brand": "Tesla", "model": "Model 3", "year": 2021},
    {"brand": "Ford", "model": "Mustang", "year": 2017},
    {"brand": "BMW", "model": "X3", "year": 2020}
]

# Algorithm: Sort cars by year (descending)
def sort_cars_by_year(cars_list):
    return sorted(cars_list, key=lambda x: x["year"], reverse=True)

# Function: Filter cars by brand
def filter_cars_by_brand(cars_list, brand_name):
    return [car for car in cars_list if car["brand"].lower() == brand_name.lower()]

# Main program
def display_cars():
    print("All cars sorted by year (newest first):")
    sorted_cars = sort_cars_by_year(cars)
    for car in sorted_cars:
        print(f"{car['brand']} {car['model']} ({car['year']})")
    
    print("\nCars by brand 'Honda':")
    honda_cars = filter_cars_by_brand(cars, "Honda")
    for car in honda_cars:
        print(f"{car['brand']} {car['model']} ({car['year']})")

# Run the program
if __name__ == "__main__":
    display_cars()
#Explanation:
Data: The cars list contains dictionaries with information about each car.
Algorithm:
sort_cars_by_year() sorts cars from newest to oldest.
Filtering function filter_cars_by_brand() finds all cars of a specific brand.
Design: Functions are used to encapsulate logic, making the code modular and maintainable.
Output:
Displays all cars sorted by year.
Shows cars of a specific brand.
