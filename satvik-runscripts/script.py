from hnn_core import neymotin_2020_model

net = neymotin_2020_model(use_data_frame=True)
print(net.conn_dataframe)
net.add_evoked_drive('evprox', mu=40, sigma=5, numspikes=1,
        location='proximal',
        weights_ampa={'L2_pyramidal': 0.01, 'L5_pyramidal': 0.01},
        synaptic_delays={'L2_pyramidal': 0.1, 'L5_pyramidal': 0.1},)