from collections import defaultdict
from hnn_core import neymotin_2020_model

synapse_tree = {
    "L2_basket": {
        "L2_pyramidal": {
            "ampa": {"soma": [0.99]}
        },
        "L2_basket": {
            "gabaa": {"soma": [0.99]}
        }
    },

    "L2_pyramidal": {
        "L2_pyramidal": {
            "nmda": {"apical_oblique": [0.9], "basal_2": [0.9], "basal_3": [0.9]},
            "ampa": {"apical_oblique": [0.9], "basal_2": [0.9], "basal_3": [0.9]}
        },
        "L2_basket": {
            "gabaa": {"soma": [0.9]},
            "gabab": {"soma": [0.9]}
        }
    },

    "L5_basket": {
        "L5_basket": {
            "gabaa": {"soma": [0.9]}
        },
        "L5_pyramidal": {
            "ampa": {"soma": [0.9]}
        },
        "L2_pyramidal": {
            "ampa": {"soma": [0.9]}
        }
    },

    "L5_pyramidal": {
        "L5_pyramidal": {
            "nmda": {"apical_oblique": [0.9], "basal_2": [0.9], "basal_3": [0.9]},
            "ampa": {"apical_oblique": [0.9], "basal_2": [0.9], "basal_3": [0.9]}
        },
        "L2_pyramidal": {
            "ampa": {
                "apical_oblique": [0.9],
                "basal_2": [0.9],
                "basal_3": [0.9],
                "apical_tuft": [0.9, 0.1, 0.3, 0.5]
            }
        },
        "L5_basket": {
            "gabaa": {"soma": [0.9]},
            "gabab": {"soma": [0.9]}
        },
        "L2_basket": {
            "gabaa": {"apical_tuft": [0.9]}
        }
    }
}

from collections import defaultdict
from hnn_core import neymotin_2020_model


net = neymotin_2020_model(synapse_tree=synapse_tree
)

from hnn_core import simulate_dipole
dpls=simulate_dipole(net,tstop=1,dt=0.025)
print(net.synapse_tree[170])
print('\n')
print('\n')
print(net.synapse_tree[35])
print('\n')
print('\n')
print(net.synapse_tree[0])
print('\n')
print('\n')
print(net.synapse_tree[135])



