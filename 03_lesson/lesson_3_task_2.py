from smartphone import Smartphone

catalog=[
    Smartphone("айфон","16","+358 40 123 4567"),
    Smartphone("nothing","00","+358 40 123 4567"),
    Smartphone("айфон","17","+358 40 123 4567"),
    Smartphone("айфон","18","+358 40 123 4567"),
    Smartphone("айфон","19","+358 40 123 4567")

]
for smartphone in catalog:
    print(f"{smartphone.marka}-{smartphone.model}.{smartphone.number}")