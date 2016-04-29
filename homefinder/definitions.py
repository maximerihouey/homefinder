"""A set of useful functions and definitions used in :module:`Homefinder`."""

from math import cos, sin, atan2, sqrt


def distance(poi_a, poi_b):
    """
    Distance between two :class:`Placemark`.

    Taken from http://andrew.hedges.name/experiments/haversine/
    """
    lat_a, lon_a = poi_a['coordinates']
    lat_b, lon_b = poi_b['coordinates']
    dlon = lon_b - lon_a
    dlat = lat_b - lat_a
    a = sin(dlat/2)**2 + cos(lat_a) * cos(lat_b) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = 6373000 * c
    return d
