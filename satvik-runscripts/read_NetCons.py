from hnn_core import neymotin_2020_model
from hnn_core.network_builder import NetworkBuilder


big_synapse_tree = {
    "L2_basket": {
        "soma": {
            0.1: {
                "ampa": ["L2_pyramidal"],
                "gabaa": ["L2_basket"]
            },
            0.99: {
                "ampa": ["L2_pyramidal"],
                "gabaa": ["L2_basket"]
            }
        }
    },

    "L2_pyramidal": {
        "apical_oblique": {
            0.1: {
                "nmda": ["L2_pyramidal"],
                "ampa": ["L2_pyramidal"]
            },
            0.99: {
                "nmda": ["L2_pyramidal"],
                "ampa": ["L2_pyramidal"]
            },
            
        },
        "basal_2": {
            0.1: {
                "nmda": ["L2_pyramidal"],
                "ampa": ["L2_pyramidal"]
            },
            0.99: {
                "nmda": ["L2_pyramidal"],
                "ampa": ["L2_pyramidal"]
            },
        },
        "basal_3": {
            0.1: {
                "nmda": ["L2_pyramidal"],
                "ampa": ["L2_pyramidal"]
            },
            0.99: {
                "nmda": ["L2_pyramidal"],
                "ampa": ["L2_pyramidal"]
            },
        },
        "soma": {
            0.1: {
                "gabaa": ["L2_basket"],
                "gabab": ["L2_basket"]
            },
            0.99: {
                "gabaa": ["L2_basket"],
                "gabab": ["L2_basket"]
            }
        }
    },

    "L5_basket": {
        "soma": {
            0.1: {
                "gabaa": ["L5_basket"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            },
             0.99: {
                "gabaa": ["L5_basket"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            }

        }
    },

    "L5_pyramidal": {
        "apical_oblique": {
            0.1: {
                "nmda": ["L5_pyramidal"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            },
            0.99: {
                "nmda": ["L5_pyramidal"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            },
        },
        "basal_2": {
            0.1: {
                "nmda": ["L5_pyramidal"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            },
            0.99: {
                "nmda": ["L5_pyramidal"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            }
        },
        "basal_3": {
            0.1: {
                "nmda": ["L5_pyramidal"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            },
            0.99: {
                "nmda": ["L5_pyramidal"],
                "ampa": ["L5_pyramidal", "L2_pyramidal"]
            }
        },
        "soma": {
            0.1: {
                "gabaa": ["L5_basket"],
                "gabab": ["L5_basket"]
            },
            0.99: {
                "gabaa": ["L5_basket"],
                "gabab": ["L5_basket"]
            }
        },
        "apical_tuft": {
            0.1: {
                "ampa": ["L2_pyramidal"],
                "gabaa": ["L2_basket"]
            },
            0.99: {
                "ampa": ["L2_pyramidal"],
                "gabaa": ["L2_basket"]
            }
        }
    }
}

net = neymotin_2020_model(orignal_synapse_creation=False,big_synapse_tree=big_synapse_tree)
builder = NetworkBuilder(net) 
for cell_type in net.gid_ranges:
    gid = list(net.gid_ranges[cell_type])[0]  
    cell = builder._cells[gid]
    cell_secs = set(cell._nrn_sections.values())

    print(f"\n{cell_type} (gid {gid}):")
    for conn_key, ncs in builder.ncs.items():
        for nc in ncs:
            seg = nc.syn().get_segment()
            if seg.sec in cell_secs:
                sec_name = seg.sec.name().split('.')[-1]
                print(f"  {conn_key}: sec={sec_name}, loc={seg.x}")