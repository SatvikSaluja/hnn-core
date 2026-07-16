from hnn_core import neymotin_2020_model, simulate_dipole
synapse_tree = {
    "L2_basket": {
        "soma": {
            0.5: {"ampa": ["L2_pyramidal"],"gabaa": ["L2_basket"]}
        }
    },
    "L2_pyramidal": {
        "apical_oblique": {
            0.5: {"nmda": ["L2_pyramidal"],"ampa": ["L2_pyramidal"]}
        },
        "basal_2": {
            0.5: {"nmda": ["L2_pyramidal"],"ampa": ["L2_pyramidal"]}
        },
        "basal_3": {
            0.5: {"nmda": ["L2_pyramidal"],"ampa": ["L2_pyramidal"]}
        },
        "soma": {
            0.5: {"gabaa": ["L2_basket"],"gabab": ["L2_basket"]}
        }
    },

    "L5_basket": {
        "soma": {
            0.5: {"gabaa": ["L5_basket"],"ampa": ["L5_pyramidal", "L2_pyramidal"]}
        }
    },

    "L5_pyramidal": {
        "apical_oblique": {
            0.5: {"nmda": ["L5_pyramidal"],"ampa": ["L5_pyramidal", "L2_pyramidal"]}
        },
        "basal_2": {
            0.5: {"nmda": ["L5_pyramidal"],"ampa": ["L5_pyramidal", "L2_pyramidal"]
            }
        },
        "basal_3": {
            0.5: {"nmda": ["L5_pyramidal"],"ampa": ["L5_pyramidal", "L2_pyramidal"]}
        },
        "soma": {
            0.5: {"gabaa": ["L5_basket"],"gabab": ["L5_basket"]
            }
        },
        "apical_tuft": {
            0.5: {"ampa": ["L2_pyramidal"],"gabaa": ["L2_basket"]}
        }
    }
    }
net1 = neymotin_2020_model(orignal_synapse_creation=False,big_synapse_tree=synapse_tree)
net1.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)
net2 = neymotin_2020_model(orignal_synapse_creation=False,big_synapse_tree=None)
net2.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)



dpl1 = simulate_dipole(net1, tstop=170, record_vsec='all')
dpl2 = simulate_dipole(net2, tstop=170, record_vsec='all')
import numpy as np
for key in ['agg', 'L2', 'L5']:
    diff = np.max(np.abs(dpl1[0].data[key] - dpl2[0].data[key]))
    print(f"{key}: {diff}")