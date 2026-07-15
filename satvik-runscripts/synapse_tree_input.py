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
net = neymotin_2020_model(orignal_synapse_creation=False,big_synapse_tree=synapse_tree)
dpl1 = simulate_dipole(net, tstop=170, record_vsec='all')
import pickle
with open("net2.pkl", "wb") as f:
    pickle.dump(net, f)
with open("dpl2.pkl", "wb") as f:
    pickle.dump(dpl1, f)

