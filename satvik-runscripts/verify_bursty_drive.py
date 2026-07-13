
#all params taken from examples script

import numpy as np
from hnn_core import jones_2009_model, simulate_dipole

net_ney = jones_2009_model(orignal_synapse_creation=True)

alpha_prox_weight = 5.4e-5
alpha_prox_tstart = 50
alpha_prox_burst_rate = 15
alpha_prox_burst_std = 20

alpha_dist_weight = 5.4e-5
alpha_dist_tstart = 50
alpha_dist_burst_rate = 15
alpha_dist_burst_std = 20


def add_bursty_drives(net):
    weights_ampa_p = {'L2_pyramidal': alpha_prox_weight,
                      'L5_pyramidal': 4.4e-5}
    syn_delays_p = {'L2_pyramidal': 0.1, 'L5_pyramidal': 1.}

    net.add_bursty_drive('alpha_prox',
                          tstart=alpha_prox_tstart,
                          burst_rate=alpha_prox_burst_rate,
                          burst_std=alpha_prox_burst_std,
                          numspikes=2,
                          spike_isi=10,
                          n_drive_cells=10,
                          location='proximal',
                          weights_ampa=weights_ampa_p,
                          synaptic_delays=syn_delays_p)

    weights_ampa_d = {'L2_pyramidal': alpha_dist_weight,
                      'L5_pyramidal': 4.4e-5}
    syn_delays_d = {'L2_pyramidal': 5., 'L5_pyramidal': 5.}

    net.add_bursty_drive('alpha_dist',
                          tstart=alpha_dist_tstart,
                          burst_rate=alpha_dist_burst_rate,
                          burst_std=alpha_dist_burst_std,
                          numspikes=2,
                          spike_isi=10,
                          n_drive_cells=10,
                          location='distal',
                          weights_ampa=weights_ampa_d,
                          synaptic_delays=syn_delays_d)


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
    add_bursty_drives(net1)
    add_bursty_drives(net2)

    dpl1 = simulate_dipole(net1, tstop=170, record_vsec='all')
    dpl2 = simulate_dipole(net2, tstop=170, record_vsec='all')

    # compare dipoles, spike times, spike gids -> any difference for any connection? if so, which one
    diff = np.max(np.abs(dpl1[0].data['agg'] - dpl2[0].data['agg']))
    print(f"conn {conn_idx}: {conn['src_type']} -> {conn['target_type']} "
          f"({conn['receptor']}, {conn['loc']})  max_diff={diff:.3e}  "
          f"allclose={np.allclose(dpl1[0].data['agg'], dpl2[0].data['agg'])}")

    del net1, net2, dpl1, dpl2