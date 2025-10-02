import numpy as np
import healpy as hp
import h5py
import matplotlib.pyplot as plt
from astropy import units

from pyradiosky import SkyModel

f1 = SkyModel()
f3 = SkyModel()
f10 = SkyModel()
f30 = SkyModel()

f1.read('exp1.0MHz_sky_map_with_absorption.skyh5')
f3.read('exp3.0MHz_sky_map_with_absorption.skyh5')
f10.read('exp10.0MHz_sky_map_with_absorption.skyh5')
f30.read('exp30.0MHz_sky_map_with_absorption.skyh5')

sky_map = {
    "1_MHz": f1.stokes[0,0],
    "3_MHz": f3.stokes[0,0],
    "10_MHz": f10.stokes[0,0],
    "30_MHz": f30.stokes[0,0],
}

d = 'data'

for k,v in sky_map.items():
    hp.mollview(np.log10(v / units.K), title=f"{k}", unit='log10(K)', coord='C')
    hp.graticule()
    plt.savefig(f"mollweide_{k}_icrs.png")
    plt.clf()
    plt.cla()
    plt.close()
