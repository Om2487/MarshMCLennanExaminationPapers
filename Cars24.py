class CarInfo:
    def __init__(self, car_id, car_name, car_type, city):
        self.__car_id = car_id
        self.__car_name = car_name
        self.__car_type = car_type
        self.__city = city


    def get_car_id(self):
        return self.__car_id
    def get_car_name(self):
        return self.__car_name
    def get_car_type(self):
        return self.__car_type
    def get_city(self):
        return self.__city
    def checkAvailability(self):
        car_name = self.__car_name.lower()
        car_type = self.__car_type.lower()
        city = self.__city.lower()
        valid_car_names = ["nissan", "ford"]
        valid_car_types = ["sedan", "suv", "muv"]
        valid_cities = ["new york", "denver", "losangels"]
        if car_name not in [x.lower() for x in valid_car_names]:
            return "Invalid Details"
        if car_type not in [x.lower() for x in valid_car_types]:
            return "Invalid Details"
        if city not in [x.lower() for x in valid_cities]:
            return "Invalid Details"

        cars_data = {
            "nissan": {
                "sedan": ("Kicks", 8400.0),
                "suv": ("Magnite", 10800.0),
                "muv": ("Terrano", 14400.0)
            },
            "ford": {
                "sedan": ("Figo", 4802.0),
                "suv": ("Eco Sport", 9605.0),
                "muv": ("Endeavour", 21600.0)
            }
        }

        available_car, price = cars_data[car_name][car_type]
        return f"Available car and price is: {available_car} and ${price}"


class UserInterface:
    @staticmethod
    def extractDetails(carDetails):
        parts = carDetails.split(":")
        if len(parts) != 4:
            return None
        car_id, car_name, car_type, city = parts
        return CarInfo(car_id.strip(), car_name.strip(), car_type.strip(), city.strip())



if __name__ == "__main__":
    user_input = input("Enter the Car Details:\n")
    car = UserInterface.extractDetails(user_input)

    if car:
        print("Car Id :", car.get_car_id())
        print("Car Name:", car.get_car_name())
        print("Car Type:", car.get_car_type())
        print("City :", car.get_city())
        print(car.checkAvailability())
    else:
        print("Invalid Details")
