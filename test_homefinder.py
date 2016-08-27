"""This module aims at helping me choose my future home in an optimal way."""

from homefinder import homefinder
import pprint

pp = pprint.PrettyPrinter(indent=1)

pm1 = homefinder.Placemark(type='apartment', coordinates=[0.0, 0.0, 0.0])
pm2 = homefinder.Placemark(type='bus_station', coordinates=[0.1, 0.1, 0.1])
pm3 = homefinder.Placemark(type='apartment', coordinates=[0.3, 0.3, 0.3])
pm4 = homefinder.Placemark(type='apartment', coordinates=[0.4, 0.4, 0.4])

print("\n")
print("Placemark 1 : ", pm1)
print("Placemark 2 : ", pm2)
print("Placemark 3 : ", pm3)
print("Placemark 4 : ", pm4)
print("\n")

hf = homefinder.Homefinder()

hf.add(pm1)
hf.add(pm2)
hf.add(pm3)
hf.add(pm4)

print("List of apartment : ", hf.get_by_type('apartment'))
print("List of bus_station : ", hf.get_by_type('bus_station'))
print("List of tramway_station : ", hf.get_by_type('tramway_station'))
print("List of velobleu_station : ", hf.get_by_type('velobleu_station'))
print("\n")

print("Importing velobleu_station ...")
hf.import_velobleu_stations("./data/velobleu.json")

pp.pprint(hf.get_by_type('velobleu_station'))
print("\n")

print("Apartment 🏠  : ", hf.get_number_of('apartment'))
print("Vélobleu  🚲  : ", hf.get_number_of('velobleu_station'))
print("Bus       🚌  : ", hf.get_number_of('bus_station'))
print("Tram      🚋  : ", hf.get_number_of('tramway_station'))
print("\n")
