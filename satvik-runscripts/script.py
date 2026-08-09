import pandas as pd
from hnn_core import neymotin_2020_model, simulate_dipole
net = neymotin_2020_model(orignal_synapse_creation=False)

net.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)
dpls=simulate_dipole(net,tstop=130,dt=0.025)
