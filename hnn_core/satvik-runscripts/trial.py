import pickle
import numpy as np
from hnn_core import jones_2009_model, simulate_dipole

net1 = jones_2009_model(orignal_synapse_creation=True)
net2 = jones_2009_model(orignal_synapse_creation=False)

net1.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},
    event_seed=274)
net2.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},
    event_seed=274)

dpl1 = simulate_dipole(net1, tstop=170, record_vsec='all')
dpl2 = simulate_dipole(net2, tstop=170, record_vsec='all')

with open("net1_orignal.pkl", "wb") as f:
    pickle.dump(net1, f)
with open("net2_syanpse_tree.pkl", "wb") as f:
    pickle.dump(net2, f)
with open("dpl1_orignal.pkl", "wb") as f:
    pickle.dump(dpl1, f)
with open("dpl2_syanpse_tree.pkl", "wb") as f:
    pickle.dump(dpl2, f)

for key in dpl1[0].data.keys():
    arr1 = np.asarray(dpl1[0].data[key])
    arr2 = np.asarray(dpl2[0].data[key])
    print(f" {key} ")
    print(" equal:", np.array_equal(arr1, arr2))
    print("allclose:", np.allclose(arr1, arr2))
    print("max  diff:", np.max(np.abs(arr1 - arr2)))
    print("mean diff:", np.mean(np.abs(arr1 - arr2)))