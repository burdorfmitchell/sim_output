import copy

import numpy as np

layouts = np.load('layouts.npy', allow_pickle=True)
layouts = layouts.item()

fnames = list(layouts.keys())

for name in fnames:
    EN_layout = layouts.get(name)
    n_ants = EN_layout.shape[0]

    print(f"generating {name} layout")
    print(f"number of antennas: {n_ants}")

    # create ENU layout, instantiated as a num_antx3 array of zeros 
    # then set first two rows to EN_layout
    layout = np.zeros(shape=(n_ants,3))
    layout[:, [0,1]] = EN_layout

    print(f"layout:\n {layout}")

    header = "Name\tNumber\tBeamID\tE\tN\tU\n\n"

    with open(name+".csv", "w") as f:
        f.write(header)
        for i, enu in enumerate(layout):
            f.write(
                f"ANT{int(i):02d}\t{i}\t0\t{enu[0]:.8f}\t{enu[1]:.8f}\t{enu[2]:.8f}\n"
            )
