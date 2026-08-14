from hnn_core import neymotin_2020_model, simulate_dipole

net_a = neymotin_2020_model(use_data_frame=True)
net_b = neymotin_2020_model(use_data_frame=False)

net_a.add_evoked_drive('evprox',mu=40, sigma=5, numspikes=1,
        location='proximal',
        weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
        synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)
net_b.add_evoked_drive('evprox',mu=40, sigma=5, numspikes=1,
        location='proximal',
        weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
        synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)
dpl_a = simulate_dipole(net_a, tstop=170)
dpl_b = simulate_dipole(net_b, tstop=170)
fig_a = dpl_a[0].plot(layer="agg", show=False)
fig_a.savefig("dipole_c.png", dpi=150)

fig_b = dpl_b[0].plot(layer="agg", show=False)
fig_b.savefig("dipole_d.png", dpi=150)
