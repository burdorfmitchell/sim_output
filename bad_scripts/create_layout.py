import copy

import numpy as np

fname = "L_array.csv"

# creating an Nx3 of antenna ENUs

# currently doing L

# points from 40 to 1000 meters with 40 meter seperation 
ant_locs = np.linspace(40,1000,25)

# create ENU layout, instantiated as a 51x3 array of zeros 
# then set first 25 E values from 40 to 1000
# then set last 25 N values from 40 to 1000
# creates L shape going East from 40 along origin, then origin, then North from 40 along origin
layout = np.zeros(shape=(50,3))
layout[:25,0] = ant_locs
layout[25:,1] = ant_locs

header = "Name\tNumber\tBeamID\tE\tN\tU\n\n"

with open(fname, "w") as f:
    f.write(header)
    for i, enu in enumerate(layout):
        f.write(
            f"ANT{int(i):02d}\t{i}\t0\t{enu[0]:.1f}\t{enu[1]:.1f}\t{enu[2]:.1f}\n"
        )
