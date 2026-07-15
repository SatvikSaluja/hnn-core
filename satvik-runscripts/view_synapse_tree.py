from hnn_core import jones_2009_model

net = jones_2009_model(orignal_synapse_creation=False)

tree = net.synapse_trees[0]
print(tree)

tree = net.synapse_trees[35]
print(tree)

tree = net.synapse_trees[135]
print(tree)

tree = net.synapse_trees[170]
print(tree)

