from collections import defaultdict
from hnn_core import neymotin_2020_model
from hnn_core.network_builder import NetworkBuilder

synapse_tree = {
    "L2_basket": {
        "L2_pyramidal": {
            "soma": {"ampa": [0.1]}
        },
        "L2_basket": {
            "soma": {"gabaa": [0.1]}
        }
    },

    "L2_pyramidal": {
        "L2_pyramidal": {
            "apical_oblique": {"nmda": [0.1], "ampa": [0.1]},
            "basal_2":        {"nmda": [0.1], "ampa": [0.1]},
            "basal_3":        {"nmda": [0.1], "ampa": [0.1]}
        },
        "L2_basket": {
            "soma": {"gabaa": [0.1], "gabab": [0.1]}
        }
    },

    "L5_basket": {
        "L5_basket": {
            "soma": {"gabaa": [0.1]}
        },
        "L5_pyramidal": {
            "soma": {"ampa": [0.1]}
        },
        "L2_pyramidal": {
            "soma": {"ampa": [0.1]}
        }
    },

    "L5_pyramidal": {
        "L5_pyramidal": {
            "apical_oblique": {"nmda": [0.1], "ampa": [0.1]},
            "basal_2":        {"nmda": [0.1], "ampa": [0.1]},
            "basal_3":        {"nmda": [0.1], "ampa": [0.1]}
        },
        "L2_pyramidal": {
            "apical_oblique": {"ampa": [0.1]},
            "basal_2":        {"ampa": [0.1]},
            "basal_3":        {"ampa": [0.1]},
            "apical_tuft":    {"ampa": [0.1]}
        },
        "L5_basket": {
            "soma": {"gabaa": [0.1], "gabab": [0.1]}
        },
        "L2_basket": {
            "apical_tuft": {"gabaa": [0.1]}
        }
    }
}



net = neymotin_2020_model(
    synapse_tree=synapse_tree,
)
net.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)

from hnn_core import simulate_dipole
dpls=simulate_dipole(net,tstop=30,dt=0.025)


    