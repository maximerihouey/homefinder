"""Test module for :class:`Homefinder`."""

from homefinder import homefinder
from pprint import pprint

hf = homefinder.Homefinder()
hf.import_velobleu_stations("./data/velobleu.json")
hf.import_bus_stations("./data/230.kml")
# print(hf.get_state())

routes = hf.gmaps.directions("15 rue Fornero Meneï, 06300 Nice",
                             "Lycée Masséna, Nice",
                             mode='walking',
                             units='metrics')

pprint(routes)

durations = [route['legs'][0]['duration']['text'] for route in routes]

pprint(durations)
