import numpy as np
import healpy as hp
import h5py
from astropy import units

from pyradiosky import SkyModel

fbase = "exp30.0MHz_sky_map_with_absorption"
print(f"fbase: {fbase}")
fname = fbase + ".hdf5"
fout = fbase + ".skyh5"

hdf5_file = h5py.File(fname, 'r')

# info
freq = 30 # MHz
print(f"freq: {freq}")
# could replace with np.ones lol
ref_freqs = np.ones(shape=hdf5_file['data'].shape)

# generate stokes array
stokes_I = hdf5_file['data'][:]
stokes_data = np.zeros(shape=(4, 1, stokes_I.shape[0]))
stokes_data[0] = stokes_I

# get spectral index
spectral_index_data = hdf5_file['spectral_index'][:]

coord_frame = 'galactic'
ordering = 'ring'
# can technically just calculate this
Nside = 64

sm = SkyModel(
    component_type = "healpix",
    nside = Nside,
    hpx_inds = list(range(len(ref_freqs))),
    stokes = stokes_data * units.K,
    freq_array = np.asarray([freq]) * units.MHz,
    spectral_type = "full",
    # linear count -- TODO: check this
    #reference_frequency = ref_freqs * units.MHz,
    #spectral_type = "spectral_index",
    #spectral_index= spectral_index_data,
    hpx_order=ordering,
    frame=coord_frame,
)

# I don't like transforming
sm.healpix_interp_transform("icrs")

sm.write_skyh5("skyh5_output/" + fout)
