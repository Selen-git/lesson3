from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S 21", "+79824568932")
phone2 = Smartphone("Apple", "iPhone", "+79378956314")
phone3 = Smartphone("Xiaomi", "Redmi Note 10", "+79255894720")
phone4 = Smartphone("Nokia", "N 95", "+79225698712")
phone5 = Smartphone("Huawei", "Honor 9 A", "+79851236987")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
  print(f"{phone.brand} {phone.model} - {phone.phone_number}")
