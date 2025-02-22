class Smartphone :
    def __init__(self, brand, model, phone_number) :
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
from smartphone import Smartphone
catalog = []
phone1 = Smartphone("Samsung", "Galaxy S 21", "+79824568932")
phone2 = Smartphone("Apple", "iPhone", "+79378956314")
phone3 = Smartphone("Xiaomi", "Redmi Note 10", "+79255894720")
