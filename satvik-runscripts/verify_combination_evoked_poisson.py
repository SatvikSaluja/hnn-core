
#all params taken from examples script

import numpy as np
from hnn_core import jones_2009_model, simulate_dipole

net_ney = jones_2009_model(orignal_synapse_creation=True)

for conn_idx, conn in enumerate(net_ney.connectivity):

    # for each iteration create a new network
    net1 = jones_2009_model(orignal_synapse_creation=True)
    net1.clear_connectivity()
    # this creates the connections old style (up to and including conn_idx)
    for c in net_ney.connectivity[:conn_idx + 1]:
        net1.add_connection(
            c["src_type"], c["target_type"], c["loc"], c["receptor"],
            c["nc_dict"]["A_weight"], c["nc_dict"]["A_delay"], c["nc_dict"]["lamtha"],
        )

    net2 = jones_2009_model(orignal_synapse_creation=False)
    net2.clear_connectivity()
    # now create with synapse tree
    for c in net_ney.connectivity[:conn_idx + 1]:
        net2.add_connection(
            c["src_type"], c["target_type"], c["loc"], c["receptor"],
            c["nc_dict"]["A_weight"], c["nc_dict"]["A_delay"], c["nc_dict"]["lamtha"],
        )

    # if just testing intra-network connections, add the same tonic bias
    net1.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)
    net2.add_evoked_drive('evprox',mu=40, sigma=5, numspikes=1,
    location='proximal',
    weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
    synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)
    weights_ampa = {'L2_pyramidal': 0.0008, 'L5_pyramidal': 0.0075}
    synaptic_delays = {'L2_pyramidal': 0.1, 'L5_pyramidal': 1.0}
    rate_constant = {'L2_pyramidal': 140.0, 'L5_pyramidal': 40.0}

    
    # if just testing intra-network connections, add the same tonic bias
    net1.add_poisson_drive(
    'poisson', rate_constant=rate_constant, weights_ampa=weights_ampa,
    location='proximal', synaptic_delays=synaptic_delays,
    event_seed=1349)
    net2.add_poisson_drive(
    'poisson', rate_constant=rate_constant, weights_ampa=weights_ampa,
    location='proximal', synaptic_delays=synaptic_delays,
    event_seed=1349)

    

    dpl1 = simulate_dipole(net1, tstop=170, record_vsec='all')
    dpl2 = simulate_dipole(net2, tstop=170, record_vsec='all')

    # compare dipoles, spike times, spike gids -> any difference for any connection? if so, which one
    diff = np.max(np.abs(dpl1[0].data['agg'] - dpl2[0].data['agg']))
    print(f"conn {conn_idx}: {conn['src_type']} -> {conn['target_type']} "
          f"({conn['receptor']}, {conn['loc']})  max_diff={diff:.3e}  "
          f"allclose={np.allclose(dpl1[0].data['agg'], dpl2[0].data['agg'])}")

    del net1, net2, dpl1, dpl2