"""
Coordinate system for HyperMap.
"""

from __future__ import absolute_import

__author__ = "Tomas Meszaros"
__email__ = "exo@tty.sk"


class CoordinateSystem(object):
    """
    A coordinate system has one or more frames.

    Parameters
    ----------
    name : string
        a user defined name
    frames : list
        list of CoordinateFrames [Time, Sky, Spectral]
    """

    def __init__(self, frames, name="CompositeSystem"):
        self.frames = frames
        self.name = name


class CoordinateFrame(object):
    """
    Base class for CoordinateFrames

    Parameters
    ----------
    system : string
        type of the frame
    num_axes : int
    axes_names : list of strings
    units : list of units
    """

    def __init__(self, system, num_axes, axes_names=None, units=None):
        """ Initialize a frame"""
        # TODO: Write type checking for @system, @num_axes, @axes_names, @units!
        self.system = system
        self.num_axes = num_axes
        self.axes_names = axes_names
        self.units = units

    def transform_to(self, other):
        """
        Transform from the current reference system to other if
        the system attribute of the two matches
        """


class SpatialFrame(CoordinateFrame):
    """
    SpatialFrame

    Parameters
    -----------------
    reference_position: list, BUT possible astropy.Time or coordinate object
                        in the future
    """

    def __init__(self, reference_position, axes_names=["",""], units=["",""]):
        super(SpatialFrame, self).__init__('Spatial', num_axes=2,
                                           axes_names=axes_names, units=units)
        self._reference_position = reference_position
