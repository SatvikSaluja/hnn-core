from hnn_core import neymotin_2020_model, simulate_dipole

net = neymotin_2020_model(use_data_frame=True)

print(net.conn_dataframe)# if u add drives , the number of rows ( depicting one connection ), will increase
# however the number of synapses doesnt increase
dpls=simulate_dipole(net,tstop=170,dt=0.025)
from neuron import h
def count_neuron_synapses():
    print(len(h.List("Exp2Syn")))

    # we can print it also
    #for x in h.List("Exp2Syn"):
    #    print(x)
count_neuron_synapses()
