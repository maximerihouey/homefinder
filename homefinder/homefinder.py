"""This module aims at helping me choose my future home in an optimal way."""

import os
import googlemaps
import json
import xmltodict


class Placemark(dict):
    """The :class:`Placemark` class."""

    def __init__(self, **keywords):
        """Constructor."""
        keys = sorted(keywords.keys())
        for kw in keys:
            self[kw] = keywords[kw]

    def add_properties(self, **keywords):
        """Add properties to the current :class:`Placemark` instance."""
        keys = sorted(keywords.keys())
        for kw in keys:
            self[kw] = keywords[kw]

    def get_type(self):
        """Return the type of the current :class:`Placemark` instance."""
        if 'type' in self:
            a_type = self['type']
        else:
            a_type = None
        return a_type

    def get_coordinates(self):
        """Return coordinates of the current :class:`Placemark` instance."""
        if 'coordinates' in self:
            coords = self['coordinates']
        else:
            coords = None
        return coords

    def get_name(self):
        """Return the name of the current :class:`Placemark` instance."""
        if 'name' in self:
            name = self['name']
        else:
            name = None
        return name

    def __str__(self):
        """String representation."""
        return super.__str__(self)


class Homefinder(object):
    """The :class:`Homefinder` class."""

    def __init__(self):
        """Constructor."""
        self.placemarks = []
        self.distance_matrix = []
        self.key = os.environ.get('HOMEFINDER_GOOGLE_API_TOKEN')
        self.gmaps = googlemaps.Client(self.key)

    def add(self, placemark):
        """Add a :class:`Placemark` to the :class:`Homefinder`."""
        self.placemarks.append(placemark)

    def add_from_file(self, filename):
        """Add :class:`Placemark` from a file."""

    def import_apartments(self, filepath):
        """Add apartments from a file."""
        with open(filepath, 'r') as inputfile:
            data = json.load(inputfile)
            for pm in data['docs']:
                self.add(Placemark(type='apartment',
                                   id=pm.id,
                                   coordinates=[pm.latitude, pm.longitude, 0.],
                                   rent=pm.rent,
                                   surface=pm.surface,
                                   extra_costs=pm.extra_costs,
                                   info=pm.info,
                                   ref=pm.ref,
                                   source=pm.url))

    def import_velobleu_stations(self, filepath):
        """Add Vélobleu stations from a file."""
        with open(filepath, 'r') as inputfile:
            data = json.load(inputfile)
            for pm in data['docs']:
                latitude, longitude = pm['geometry']['coordinates']
                self.add(Placemark(type='velobleu_station',
                                   id=int(pm['IDENT']),
                                   size=int(pm['NBR_PT_ACC']),
                                   coordinates=[latitude, longitude, 0.0]))

    def import_bus_stations(self, filepath):
        """Add bus stations from a file."""
        with open(filepath, 'r') as inputfile:
            doc = xmltodict.parse(inputfile.read())
            for pm in doc['kml']['Document']['Placemark']:
                coords = [float(a) for a in
                          pm['Point']['coordinates'].split(',')]
                self.add(Placemark(type='bus_station',
                                   name=pm['name'],
                                   id=int(pm['id']),
                                   coordinates=coords))

    def get_by_type(self, typename):
        """Retrieve all placemarks of type :param:`typename`."""
        return [pm for pm in self.placemarks if pm['type'] == typename]

    def get_number_of(self, typename):
        """Return number of placemarks of type :param:`typename`."""
        return len(self.get_by_type(typename))

    def get_state(self):
        """Give the state of the current :class:`Homefinder` instance."""
        types = set([pm['type'] for pm in self.placemarks])
        return {typename: self.number_of(typename) for typename in types}

    def create_distance_matrix(self):
        """Distance matrix of the current :class:`Homefinder` instance."""
        apartments = self.get_by_type('apartment')
        bus_stations = self.get_by_type('bus_station')
        origins = [pm['coordinates'][0:-1] for pm in apartments]
        destinations = [pm['coordinates'][0:-1] for pm in bus_stations]
        distance_matrix = self.gmaps.distance_matrix(origins,
                                                     destinations,
                                                     mode='walking',
                                                     units='metric')
        return distance_matrix

    def display_map(self):
        """Display a map of the facilities."""
        # ToDo
        pass

    def optimize(self):
        """Find the optimal home."""
        # ToDo
        # First we retrieve the apartments
        apartments = self.get_by_type('apartment')
        results = {}
        # k = 0
        # For each apartment, we compute the distance_matrix to the nearest
        # placemark of each type, and we store it in the results dictionary.
        for aparment in apartments:
            # foo = results[k] = {}
            # print(foo)
            pass
        return results

    def __str__(self):
        """String representation."""
        return str(self.placemarks)
