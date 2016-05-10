import numpy as np
import matplotlib.pyplot as plt

width = 3
length = 3
photons_per_bunch = 100
n_bunches = 1000


x = np.arange(30) * width * 1.5
y = np.arange(20) * length * 1.5


x_bunch = np.random.choice(x, n_bunches)
y_bunch = np.random.choice(y, n_bunches)


x_photon = np.random.uniform(
    x_bunch - width/2, x_bunch + width/2,
    (photons_per_bunch, n_bunches)
)
y_photon = np.random.uniform(
    y_bunch - length/2, y_bunch + length/2,
    (photons_per_bunch, n_bunches)
)

t_photon = np.random.normal(np.arange(n_bunches), 5e-9, (photons_per_bunch, n_bunches))


np.savetxt(
    'toy_photons.csv',
    np.column_stack([
        x_photon.T.ravel(),
        y_photon.T.ravel(),
        t_photon.T.ravel(),
    ]),
    delimiter=',',
    header='x,y,t',
)
