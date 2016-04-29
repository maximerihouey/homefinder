"""This module aims at helping me choose my future home in an optimal way."""

import json


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

    def type(self):
        """Return the type of the current :class:`Placemark` instance."""
        if 'type' in self:
            a_type = self['type']
        else:
            a_type = 'undefined'
        return a_type

    def __str__(self):
        """String representation."""
        return super.__str__(self)


class Homefinder(object):
    """The :class:`Homefinder` class."""

    def __init__(self):
        """Constructor."""
        self.placemarks = []

    def add(self, placemark):
        """Add a :class:`Placemark` to the :class:`Homefinder`."""
        self.placemarks.append(placemark)

    def add_from_file(self, filename):
        """Add :class:`Placemark` from a file."""

    def add_velobleu(self, filepath):
        """Add Vélobleu stations from a file."""
        with open(filepath, 'r') as inputfile:
            data = json.load(inputfile)
            for pm in data['docs']:
                latitude, longitude = pm['geometry']['coordinates']
                self.add(Placemark(type='velobleu_station',
                                   coordinates=[latitude, longitude, 0.0]))

    def get_by_type(self, typename):
        """Retrieve all placemarks of type :param:`typename`."""
        return [pm for pm in self.placemarks if pm['type'] == typename]

    def number_of(self, typename):
        """Return number of placemarks of type :param:`typename`."""
        return len(self.get_by_type(typename))

    def display_map(self):
        """Display a map of the facilities."""
        # ToDo

    def optimize(self):
        """Find the optimal home."""
        # ToDo

    def __str__(self):
        """String representation."""
        return str(self.placemarks)
