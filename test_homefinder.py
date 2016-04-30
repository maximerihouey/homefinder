"""Test module for :class:`Homefinder`."""

from homefinder import homefinder

hf = homefinder.Homefinder()
hf.import_velobleu_stations("./data/velobleu.json")
hf.import_bus_stations("./data/230.kml")
print(hf.state())
