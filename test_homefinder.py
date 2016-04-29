"""Test module for :class:`Homefinder`."""

from homefinder import homefinder

pm1 = homefinder.Placemark(type='bus_station', coordinates=[1.2, 2.0, 0.0])
pm2 = homefinder.Placemark(type='apartment', coordinates=[1.3, 1.2, 2.0])
pm3 = homefinder.Placemark(type='tramway_station', coordinates=[1.1, 1.2, 0.0])
print(pm1)

hf = homefinder.Homefinder()
hf.add(pm1)
hf.add(pm2)
hf.add(pm3)

print(hf.get_by_type('apartment'))
print(hf.get_by_type('bus_station'))
print(hf.get_by_type('tramway_station'))
print(hf.get_by_type('velobleu_station'))

hf.add_velobleu("./data/velobleu.json")

print(hf.get_by_type('velobleu_station'))
print(hf.number_of('velobleu_station'))
print(hf.number_of('apartment'))
print(hf.number_of('bus_station'))
print(hf.number_of('tramway_station'))
