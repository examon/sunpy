"""
HyperMap
"""

from __future__ import absolute_import

import matplotlib.pyplot as plt

import sunpy.visualization as viz

__author__ = "Tomas Meszaros"
__email__ = "exo@tty.sk"

class HyperMap(object):
    """
    HyperMap

    Parameters
    ----------
    data : numpy.ndarray
        data
    coordinate_system : CoordinateSystem
        CoordinateSystem object
    header : list
        header
    """

    def __init__(self, data, coordinate_system, header):
        self.data = data
        self.system = coordinate_system
        self.header = header
    
    def plot(self, animate=False):
        """
        Plot a HyperMap
        
        Parameters
        ----------
        animate: int
            Axis of underlying ndarray to animate
        """
        #TODO: Make animate more cleverer
        naxis = len(self.system.frames)
        
        if naxis == 1:
            #Plot some thing
            pass
        elif naxis == 2:
            #imshow something
            pass
        elif naxis == 3:
            if isinstance(animate, bool) and animate:
                raise ValueError("What axis to animate fool?!")
            #What axis are we animating over
            fig, ax = plt.subplots(1)
            ani = viz.animate_array(self.data, animate, axes=ax, cmap=plt.get_cmap('gray'),
                                    norm='dynamic', extent=None, interval=200, colorbar=False)

            return ani
            
        else:
            raise ValueError("Can't plot this hypermap, please slice it")
        
